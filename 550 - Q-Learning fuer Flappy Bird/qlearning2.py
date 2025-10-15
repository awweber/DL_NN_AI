import flappy
import numpy as np
import sys

# Hyperparameter für Q-Learning
rewardAlive = 1 # Belohnung pro Frame (überleben)
rewardKill = -10000 # Bestrafung bei Tod
rewardPassPipe = 500 # Belohnung für das Passieren einer Pipe
alpha = 0.2 # Lernrate
gamma = 0.9 # Diskontfaktor

# Q-Table Q_new(s_t, a_t) 
# = (1 - alpha) * Q(s_t, a_t) + alpha [ reward r_t + gamma * max( Q(s_{t+1}, a_{t}) ) ]
Q = {}

# Zustand aus den Parametern erzeugen (s_t) = zusammengefasste Repräsentation der Spielumgebung 
# z.B. 0_156_400_-189_544_-147 (ohne lower pipes)
def paramsToState(params):
    return str(params['playerVelY']) + "_" + str(params["playery"]) + "_" + \
        str(int(params["upperPipes"][0]['x'])) + "_" + str(int(params["upperPipes"][0]['y'])) + "_" + \
        str(int(params["upperPipes"][1]['x'])) + "_" + str(int(params["upperPipes"][1]['y']))

# Print des extrahierten Zustands s_t
print(paramsToState({'playerVelY': 0, 'playery': 156,
                     'upperPipes': [{'x': 400, 'y': -189}, {'x': 544.0, 'y': -147}], 
                     'lowerPipes': [{'x': 400, 'y': 231}, {'x': 544.0, 'y': 273}]}))
sys.exit()

# Callback-Funktionen
def onGameover(gameInfo):
    print(gameInfo)

def shouldEmulateKeyPress(params):
    print(params)
    return np.random.choice([False, True], p=[0.9, 0.1])

flappy.main(shouldEmulateKeyPress, onGameover)