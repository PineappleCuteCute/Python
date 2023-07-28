import gym
import MachineLearning.numpy as np

class SolarisEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(SolarisEnv, self).__init__()

        # define action space and observation space
        self.action_space = gym.Space.Discrete(3) # type: ignore # move left, stay, move right
        self.observation_space = gym.Space.Box(low=0, high=255, shape=(210, 160, 3), dtype=np.uint8) # type: ignore

        # initialize game state
        self.game = SOLARIS_XHDTYPE() # type: ignore

    def step(self, action):
        # execute action and get new game state
        if action == 0:
            self.game.move_left()
        elif action == 2:
            self.game.move_right()
        reward = self.game.get_score()
        obs = self.game.get_state()
        done = self.game.is_game_over()
        info = {}

        return obs, reward, done, info
    

    def reset(self):
        # reset game state
        self.game = SSOLARIS_XHDTYPE() # type: ignore
        obs = self.game.get_state()

        return obs

    def render(self, mode='human'):
        # display game state
        self.game.show_game()

# Q-learning agent
class QLearningAgent():
    def __init__(self, alpha, gamma, epsilon, actions):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = actions
        self.q_table = {}

    def get_action(self, state):
        if np.random.uniform() < self.epsilon:
            # explore
            return np.random.choice(self.actions)
        elif state in self.q_table:
            # exploit
            q_values = self.q_table[state]
            return np.argmax(q_values)
        else:
            # unknown state
            return np.random.choice(self.actions)

    def learn(self, state, action, reward, next_state, done):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))

        if done:
            self.q_table[state][action] += self.alpha * (reward - self.q_table[state][action])
        else:
            if next_state not in self.q_table:
                self.q_table[next_state] = np.zeros(len(self.actions))
            td_target = reward + self.gamma * np.max(self.q_table[next_state])
            td_error = td_target - self.q_table[state][action]
            self.q_table[state][action] += self.alpha * td_error

# train Q-learning agent
def train(agent, env, episodes):
    for episode in range(episodes):
        state = env.reset()
        done = False

        while not done:
            action = agent.get_action(state)
            next_state, reward, done, _ = env.step(action)
            agent.learn(state, action, reward, next_state, done)
            state = next_state

        print("Episode {}: score = {}".format(episode, reward))

# test Q-learning agent
def test(agent, env):
    state = env.reset
done = False
total_reward = 0

while not done:
    action = agent.get_action(State)
    next_state, reward, done, _ = environ.step(action) # type: ignore
    total_reward += reward
    state = next_state

print("Total reward = {}".format(total_reward))

if name == 'main':
# initialize environment and agent
environb = SolarisEnv()
actions = [0, 1, 2] # move left, stay, move right
agent = QLearningAgent(alpha=0.5, gamma=0.95, epsilon=0.1, actions=actions)

# train and test agent
train(agent, environb, episodes=100)
test(agent, environb)

