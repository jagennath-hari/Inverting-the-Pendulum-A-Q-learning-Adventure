# Inverting the Pendulum: A Q-learning Adventure
Developed model-free controller using Q-learning to solve the inverted pendulum problem.

<p align = 'center'><img src ='assets/inverted_pendulum.gif'></p>   
<p align = 'center'><em>Simulation of Simple Pendulum</em></p> 

## Q-table

The Q-learning algorithm is implemented with a table, the dimension of the Q-table will be of dimension $\mathbf{50x50x3}$ to accomodate this $\mathbf{50}$ discretized states for $\theta$ and $\mathbf{50}$ for $\omega$.
<p align = 'center'><img src ='assets/Q-table.png' width="550" height="300" ></p>   
<p align = 'center'><em>Q-table</em></p> 

## Results
The results in the form of graphs are visualized below.

Solarized dark             |  Solarized Ocean
:-------------------------:|:-------------------------:
![](assets/Q-table.png)  |  ![](assets/Q-table.png)
