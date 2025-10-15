# Vorbereitung auf Q-Learning für Flappy Bird
# Basierend auf dem Flappy Bird Klon von @sourabhv
# Ausgabe der Spielparameter in der Konsole
# Zufälliges Drücken der Taste mit einer Wahrscheinlichkeit von 10%
# (1) Flappy Bird Klon starten mit flappy.main()
# (2) Spielparameter in der Konsole ausgeben
# (3) Zufälliges Drücken der Taste mit einer Wahrscheinlichkeit von 10%
# (4) Game Over info in der Konsole ausgeben

import flappy
import numpy as np

# Callback-Funktion, die bei Game Over aufgerufen wird
def onGameover(gameInfo):
    # Game Over info in der Konsole ausgeben
    print(gameInfo)

# Callback-Funktion, die entscheidet, ob die Taste gedrückt werden soll
def shouldEmulateKeyPress(params):
    # Spielparameter in der Konsole ausgeben
    # print(params)
    # Zufälliges Drücken der Taste mit einer Wahrscheinlichkeit von 10%
    return np.random.choice([False, True], p=[0.9, 0.1])

# Flappy Bird Klon starten mit flappy.main() mit den Callback-Funktionen
flappy.main(shouldEmulateKeyPress, onGameover)