# Inverting the Pendulum: A Q-learning Adventure
Developed model-free controller using Q-learning to solve the inverted pendulum problem.

Simulation of simple pendulum

<p float="center">
  <img src="assets/inverted_pendulum.gif" width="400" height="350" />
  <img src="assets/inverted_pendulum2.gif" width="400" height="350" />
</p> 

## Q-table

The Q-learning algorithm is implemented with a table, the dimension of the Q-table will be of dimension $\mathbf{50x50x3}$ to accomodate this $\mathbf{50}$ discretized states for $\theta$ and $\mathbf{50}$ for $\omega$. $u$ is limited to $3$ values for simplicity.
<p align = 'center'><img src ='assets/Q-table.png' width="550" height="300" ></p>   
<p align = 'center'><em>Q-table</em></p> 

## Algorithm


## Results
The results in the form of graphs are visualized below.
<p float="center">
  <img src="assets/u=4(state).png" width="400" height="350" />
  <img src="assets/u=4(control).png" width="400" height="350" />
</p>

The learning curves show the TD-error and instantaneous cost during the learning process.
<p float="center">
  <img src="assets/u=4(error).png" width="400" height="350" />
  <img src="assets/u=4(cost).png" width="400" height="350" /> 
</p>

The policy and value function learnt are vizualized to give a better of the learning process.
<p float="center">
  <img src="assets/u=4(policy).png" width="400" height="350" />
  <img src="assets/u=4(value).png" width="400" height="350" /> 
</p>

## Report
To read a detailed report, click [HERE](assets/Report.pdf)
