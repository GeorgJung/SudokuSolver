'''
Created on 15.02.2021

__updated__='2021-05-08'

@author: jung
'''

import numpy as np

# Puzzle from cover of Sudoku
Pzzl00 = np.array([[0, 0, 0, 0, 8, 0, 9, 0, 0],
                   [4, 0, 2, 3, 0, 0, 6, 0, 0],
                   [9, 0, 1, 5, 0, 0, 0, 0, 3],
                   [0, 0, 4, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 6, 7, 8, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [1, 0, 0, 0, 0, 6, 2, 0, 7],
                   [0, 0, 9, 0, 0, 1, 3, 0, 5],
                   [0, 0, 3, 0, 4, 0, 0, 0, 0]])

# Puzzle number 91 from Sudoku book
Pzzl91 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 2, 0, 0, 0, 0, 3],
                   [4, 0, 0, 9, 0, 0, 7, 0, 0],
                   [0, 7, 0, 0, 0, 0, 0, 0, 8],
                   [0, 0, 5, 0, 4, 0, 0, 0, 0],
                   [9, 0, 8, 0, 0, 1, 0, 6, 0],
                   [3, 0, 9, 0, 0, 0, 0, 0, 2],
                   [0, 0, 0, 6, 0, 0, 3, 0, 5],
                   [0, 6, 0, 0, 0, 7, 0, 0, 4]])

# Puzzle from Alverde magazine February 2021
Feb2021 = np.array([[0, 0, 7, 0, 0, 0, 1, 0, 0],
                    [0, 3, 0, 0, 0, 0, 0, 2, 0],
                    [1, 0, 0, 5, 0, 9, 0, 0, 4],
                    [0, 0, 2, 0, 5, 0, 6, 0, 0],
                    [0, 6, 0, 0, 0, 0, 0, 5, 0],
                    [0, 0, 9, 0, 3, 0, 7, 0, 0],
                    [6, 0, 0, 4, 0, 2, 0, 0, 5],
                    [0, 4, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 8, 0, 0, 0, 3, 0, 0]])

Mar2021 = np.array([[2, 0, 0, 1, 0, 0, 0, 0, 7],
                    [0, 3, 7, 0, 0, 5, 8, 0, 0],
                    [0, 0, 0, 0, 4, 0, 0, 9, 0],
                    [0, 0, 0, 0, 0, 2, 3, 0, 0],
                    [8, 0, 0, 0, 0, 0, 0, 0, 6],
                    [0, 0, 5, 9, 0, 0, 0, 0, 0],
                    [0, 2, 0, 0, 6, 0, 0, 0, 0],
                    [0, 0, 8, 7, 0, 0, 5, 1, 0],
                    [9, 0, 0, 0, 0, 3, 0, 0, 4]])

Apr2021 = np.array([[8, 0, 0, 0, 7, 6, 4, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0, 0, 0],
                    [9, 0, 0, 0, 0, 0, 5, 8, 1],
                    [0, 4, 6, 5, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 7, 2, 4, 0],
                    [3, 7, 2, 0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0, 0, 0, 0, 6],
                    [0, 0, 1, 8, 9, 0, 0, 0, 4]])

May2021 = np.array([[0, 4, 0, 0, 0, 0, 0, 9, 0],
                    [6, 7, 0, 0, 2, 0, 0, 8, 1],
                    [0, 0, 0, 7, 0, 8, 0, 0, 0],
                    [0, 0, 5, 0, 4, 0, 2, 0, 0],
                    [0, 1, 0, 8, 0, 3, 0, 7, 0],
                    [0, 0, 9, 0, 6, 0, 4, 0, 0],
                    [0, 0, 0, 1, 0, 5, 0, 0, 0],
                    [9, 5, 0, 0, 8, 0, 0, 3, 2],
                    [0, 8, 0, 0, 0, 0, 0, 6, 0]])

attempts = 0


def solve(Pzzl):
    global attempts
    # find the first empty square
    for x in range(9):
        for y in range(9):
            if Pzzl[y][x]:
                # This is the last square, and it is not empty. We are done!
                if (x, y) == (8, 8):
                    return True
                # This square is not the last and also not empty. Try the next!
                continue

            # Found the first empty square. Try all ciphers from 1 to 9!
            for l in range(1, 10):
                # If cipher is already in the column, try next!
                if l in Pzzl[y]:
                    continue
                # If cipher is already in the row, try next!
                if l in Pzzl[:, x]:
                    continue
                # If cipher is already in the quadrant, try next!
                (i, j) = (x - x % 3, y - y % 3)
                if l in Pzzl[j:j + 3, i:i + 3]:
                    continue
                # Cipher is not used yet. Put it on the square!
                Pzzl[y][x] = l
                # This is the last square. We are done!
                if (x, y) == (8, 8):
                    return True
                # This is not the last square. Can we solve the puzzle with the current cipher added?
                if solve(Pzzl):
                    # Yes, we solved it!
                    return True
                # No, that did not work. Try the next cipher.

            # No cipher was able to solve the puzzle. Reset to zero and backtrack!
            Pzzl[y][x] = 0
            attempts += 1
            return False


Pzzl = May2021

print(Pzzl)
print()

if solve(Pzzl):
    print(Pzzl)
    print("Attempts: {}".format(attempts))
else:
    print("No solution found!")

