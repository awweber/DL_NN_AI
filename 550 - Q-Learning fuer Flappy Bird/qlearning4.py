import flappy
import numpy as np
import sys
from collections import defaultdict

# Hyperparameter für Q-Learning
rewardAlive = 1 # Belohnung pro Frame (überleben)
rewardKill = -10000 # Bestrafung bei Tod
alpha = 0.2 # Lernrate
gamma = 0.9 # Diskontfaktor

# Q-Table Q_new(s_t, a_t) 
# = (1 - alpha) * Q(s_t, a_t) + alpha [ reward r_t + gamma * max( Q(s_{t+1}, a_{t}) ) ]
# Q[state] = (Nicht springen, springen)
Q = defaultdict(lambda: [0, 0]) # Q[state] = (Q(state, no-flap), Q(state, flap))


# Zustand aus den Parametern erzeugen (s_t) = zusammengefasste Repräsentation der Spielumgebung 
# z.B. 0_156_400_-189_544_-147 (ohne lower pipes)
def paramsToState(params):
    return str(params['playerVelY']) + "_" + str(params["playery"]) + "_" + \
        str(int(params["upperPipes"][0]['x'])) + "_" + str(int(params["upperPipes"][0]['y'])) + "_" + \
        str(int(params["upperPipes"][1]['x'])) + "_" + str(int(params["upperPipes"][1]['y']))


def onGameover(gameInfo):
    print(gameInfo)

oldState = None
oldAction = None

def shouldEmulateKeyPress(params):
    global oldState
    global oldAction

    print(Q)

    state = paramsToState(params)
    estReward = Q[state]


    # Q updaten für die vorherige Aktion
    #  -> Die vorherige Aktion war erfolgreich!
    prevReward = Q[oldState]
    index = None
    if oldAction == False:
        index = 0
    else: 
        index = 1
    
    # Q_new(s_t, a_t)
    # = (1 - alpha) * Q(s_t, a_t) + alpha [ reward r_t + gamma * max( Q(s_{t+1}, a_{t}) )
    prevReward[index] = (1 - alpha) * prevReward[index] + \
        alpha * (rewardAlive + gamma * max(estReward))
    Q[oldState] = prevReward
    
    # 
    oldState = state
    if estReward[0] >= estReward[1]:
        oldAction = False
        return False
    else:
        oldAction = True
        return True


flappy.main(shouldEmulateKeyPress, onGameover)