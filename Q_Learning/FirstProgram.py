import os
import gym
import numpy as np

# #khoi tao moi truong CartPole
env = gym.make("CartPole-v1")


# (next_state, reward, terminated, truncated,()) = env.step(1);
# q_table_size = 20
# q_table_segment_size = (env.observation_space.high[0] - env.observation_space.low[0]) / q_table_size
q_learning_rate = 0.1
q_discount_rate = 0.9
q_no_of_eps = 500

q_goal = 30

CART_POS_LOW = env.observation_space.low[0]
POLE_ANGLE_LOW = env.observation_space.low[2]
Q_table_cartpos_segment = (env.observation_space.high[0] - env.observation_space.low[0]) / 20
Q_table_poleangle_segment = (env.observation_space.high[2] - env.observation_space.low[2]) / 20
q_table_lines = 400
max_episode = 0
max_count = 0


def ConvertStatePosToDiscrete(state):
    a = (state[0] - CART_POS_LOW) // Q_table_cartpos_segment
    b = (state[2] - POLE_ANGLE_LOW) // Q_table_poleangle_segment
    a = np.int16(a)
    b = np.int16(b)
    return (a,b)

def ConvertDiscreteToIndex(discrete):
    i = discrete[0] * 20 + discrete[1]
    return i

q_table = [[0 for x in range(2)] for y in range(400)]

# for i in range(0,400):
#     q_table[i] = [np.random.random(), np.random.random()]


if os.path.exists("FirstProgram.txt"):
    f = open("FirstProgram.txt", 'r')
    lines = f.readlines()
    i = 0
    for line in lines:
        q_table[i] = eval(line)
        i += 1


number_of_complete = 0

for ep in range(q_no_of_eps):
    print("Episode = ", ep, "************************************************************")
    (current_state, ()) = env.reset()
    done = False
    count = 0

    while not done:
        count += 1
        stateIndex = ConvertDiscreteToIndex(ConvertStatePosToDiscrete(current_state))
        print(stateIndex)
        print(q_table[stateIndex])

        if q_table[stateIndex][0] > q_table[stateIndex][1]:
            action = 0
        else:
            action = 1
        print(action)

        next_state = env.step(action=action)
        print(next_state[0])

        reward = next_state[1]
        done = next_state[2]

        if done: 
            print(count)
            if(count > q_goal):
                print("\n ok=========================================")
                number_of_complete += 1
                if(max_count < count):
                    max_count = count
                    max_episode = ep
            else:
                print("Failed")
                new_q_value = (1 - q_learning_rate) * q_table[stateIndex][action] + q_learning_rate * ((-10) * reward + q_discount_rate * next_q_value)
                q_table[stateIndex][action] = new_q_value
        else: 
            nextStateIndex = ConvertDiscreteToIndex(ConvertStatePosToDiscrete(next_state[0]))
            if q_table[nextStateIndex][0] > q_table[nextStateIndex][1]:
                next_q_value = q_table[nextStateIndex][0]
            else: 
                next_q_value = q_table[nextStateIndex][1]

            new_q_value = (1 - q_learning_rate) * q_table[stateIndex][action] + q_learning_rate * (reward + q_discount_rate * next_q_value)

            q_table[stateIndex][action] = new_q_value
            
            current_state = next_state[0]
            
print(number_of_complete)
print(max_count, "-", max_episode)

f = open("FirstProgram.txt", "w")
for i in range(0,400):
    txt = "{}\n"
    f.writelines(txt.format(q_table[i]))
f.close()

