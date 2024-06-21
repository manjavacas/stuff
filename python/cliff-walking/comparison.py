from cliff_env import CliffWalk

from sarsa import SARSA
from q_learning import QLearning
from expected_sarsa import ExpSARSA


import matplotlib.pyplot as plt


env = CliffWalk()

sarsa = SARSA(env)
qlearn = QLearning(env)
expsarsa = ExpSARSA(env)

n_episodes = 500

sarsa.learn(n_episodes, plot=False)
qlearn.learn(n_episodes, plot=False)
expsarsa.learn(n_episodes, plot=False)

plt.figure(figsize=(10, 6))
plt.plot(sarsa.total_rewards, label='SARSA')
plt.plot(qlearn.total_rewards, label='Q-learning')
plt.plot(expsarsa.total_rewards, label='Expected SARSA')
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.title('SARSA vs. Q-learning vs. Expected SARSA')
plt.legend()
plt.grid(True)
plt.show()
