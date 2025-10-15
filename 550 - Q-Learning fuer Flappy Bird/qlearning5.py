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


def paramsToState(params):
    return str(params['playerVelY']) + "_" + str(params["playery"]) + "_" + \
        str(int(params["upperPipes"][0]['x'])) + "_" + str(int(params["upperPipes"][0]['y'])) + "_" + \
        str(int(params["upperPipes"][1]['x'])) + "_" + str(int(params["upperPipes"][1]['y']))

# Alte State und Action speichern
# für Q-Updatem initial=None
oldState = None
oldAction = None

# Wird aufgerufen, wenn das Spiel vorbei ist
# Q updaten für Gameover (Agent ist gestorben = negative Belohnung/Bestrafung)
def onGameover(gameInfo):
    global oldState
    global oldAction

    # Q updaten für die vorherige Aktion
    #  -> Die vorherige Aktion war nicht erfolgreich!
    prevReward = Q[oldState]
    index = None
    if oldAction == False:
        index = 0
    else: 
        index = 1
    
    # Q_new(s_t, a_t)
    # = (1 - alpha) * Q(s_t, a_t) 
    # + alpha [ reward r_t + gamma * max( Q(s_{t+1}, a_{t}) )
    prevReward[index] = (1 - alpha) * prevReward[index] + \
        alpha * rewardKill
    Q[oldState] = prevReward

    print(Q)

    # Reset oldState und oldAction für neues Spiel
    oldState = None
    oldAction = None


# Update Q-Table und entscheide, ob geflapt werden soll
def shouldEmulateKeyPress(params):
    global oldState
    global oldAction

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
    # = (1 - alpha) * Q(s_t, a_t) 
    # + alpha [ reward r_t + gamma * max( Q(s_{t+1}, a_{t}) )
    prevReward[index] = (1 - alpha) * prevReward[index] + \
        alpha * (rewardAlive + gamma * max(estReward))
    Q[oldState] = prevReward
    
    oldState = state
    if estReward[0] >= estReward[1]:
        oldAction = False
        return False
    else:
        oldAction = True
        return True


flappy.main(shouldEmulateKeyPress, onGameover)