# Inverting the Pendulum: A Q-learning Adventure
Developed model-free controller using Q-learning to solve the inverted pendulum problem.

<p align = 'center'><img src ='assets/inverted_pendulum.gif'></p>   
<p align = 'center'><em>Simulation of Simple Pendulum</em></p> 

## Q-table

The Q-learning algorithm is implemented with a table. For the action value function given in equation, $Q(x_t, u_t)$ the assumptions are made such that $u$ can take only **three** possible values. For states $\theta$ can take any value in the range of ${[0,2\pi]}$ and that $\omega$ can take any value between ${[-6,6]}$. In order to build the table, we will need to discretize the states. So for the learning algorithm, we will use $\mathbf{50}$ discretized states for $\theta$ and $\mathbf{50}$ for $\omega.$ Hence the dimension of the Q-table will be of dimension $\mathbf{50x50x3}$.

<p align = 'center'><img src ='assets/Q-table.png' width="550" height="300" ></p>   
<p align = 'center'><em>Q-table</em></p> 
