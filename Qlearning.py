import numpy as np
import pendulum


class qSolver:
    def __init__(self, u = 4, learning_rate = 0.1, epsilon_greedy = 0.1):
        # Creating a discretized states and control for look up
        self.u = np.array([-u, 0, u])
        self.theta = np.linspace(0, 2 * np.pi, 50, endpoint = False)
        self.omega = np.linspace(-pendulum.MAX_VELOCITY, pendulum.MAX_VELOCITY, 50)
        # Creating Q-table
        self.q_table = np.zeros([50, 50, 3])
        # Creating policy and value functions
        self.value_function = np.zeros([50, 50])
        self.policy = np.zeros([50, 50])
        # hyper parameters
        self.epsilon = epsilon_greedy
        self.lr = learning_rate
        self.alpha = 0.99
        # cost
        self.costEpisode = []
        self.td_error = []

    @staticmethod
    def get_next_state(x, u):
        return pendulum.get_next_state(x, u)

    @staticmethod
    def get_cost(x, u):
        return (x[0] - np.pi) ** 2 + (0.01 * (x[1] ** 2)) + (0.0001 * (u ** 2))

    def getIdx(self, state):
        return np.argmin(np.abs(self.theta - state[0])), np.argmin(np.abs(self.omega - state[1]))

    def get_policy_and_value_function(self):
        for theta in range(50):
            for omega in range(50):
                self.value_function[theta, omega] = self.q_table[theta, omega, np.argmin(self.q_table[theta, omega])]
                self.policy[theta, omega] = np.argmin(self.q_table[theta, omega])
        self.value_function, self.policy = self.value_function.transpose()[::-1], self.policy.transpose()[::-1]

    def train(self, epoch=1000):
        for episode in range(epoch):
            cost = 0
            td_error = 0
            state = np.array([0, 0])
            thetaIdx, omegaIdx = self.getIdx(state)
            for step in range(100):
                controlIdx = np.random.randint(0, 3) if np.random.uniform(0, 1) < self.epsilon else np.argmin(self.q_table[thetaIdx, omegaIdx, :])
                nextState = self.get_next_state(state, self.u[controlIdx])
                nextThetaIdx, nextOmegaIdx = self.getIdx(nextState)
                error = self.get_cost(state, self.u[controlIdx]) + self.alpha * np.min(self.q_table[nextThetaIdx, nextOmegaIdx, :]) - self.q_table[thetaIdx, omegaIdx, controlIdx]
                self.q_table[thetaIdx, omegaIdx, controlIdx] = self.q_table[thetaIdx, omegaIdx, controlIdx] + self.lr * error
                thetaIdx, omegaIdx, state = nextThetaIdx, nextOmegaIdx, nextState
                cost += self.get_cost(state, self.u[controlIdx])
                td_error += error
            self.costEpisode.append(cost)
            self.td_error.append(td_error)
        self.get_policy_and_value_function()

    def inverted_controller(self, state):
        thetaIdx, omegaIdx = self.getIdx(state)
        return self.u[np.argmin(self.q_table[thetaIdx, omegaIdx, :])]
