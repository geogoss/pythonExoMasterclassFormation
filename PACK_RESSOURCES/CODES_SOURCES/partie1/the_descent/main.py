import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

hauteur_montages = [2, 6, 7, 9, 5, 4, 3, 2]

# game loop
while True:
    max = -1
    imax = -1
    for i in range(8):
        mountain_h = hauteur_montages[i]
        if mountain_h > max:
            max = mountain_h
            imax = i
        print("H=", mountain_h, file=sys.stderr, flush=True)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    print(imax)
