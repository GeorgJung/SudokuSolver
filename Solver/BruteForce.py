'''
Created on 15.02.2021

__updated__='2022-08-13'

@author: jung
'''

import numpy as np

# Empty Puzzle
Pzzlxx = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]])

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

# Puzzles from Alverde magazine since February 2021
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

Jun2021 = np.array([[0, 0, 1, 0, 0, 0, 0, 2, 0],
                    [0, 2, 0, 3, 0, 0, 6, 0, 8],
                    [4, 0, 0, 0, 5, 0, 0, 1, 0],
                    [0, 6, 0, 7, 0, 0, 0, 0, 0],
                    [0, 0, 8, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 2, 0, 3, 0],
                    [0, 3, 0, 0, 4, 0, 0, 0, 5],
                    [5, 0, 4, 0, 0, 6, 0, 7, 0],
                    [0, 7, 0, 0, 0, 0, 8, 0, 0]])

Jul2021 = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 7, 0, 4, 5, 0, 0, 0, 0],
                    [0, 0, 6, 0, 8, 0, 1, 5, 0],
                    [0, 5, 0, 0, 0, 2, 0, 1, 0],
                    [8, 0, 0, 0, 0, 0, 0, 0, 6],
                    [0, 3, 0, 5, 0, 0, 0, 8, 0],
                    [0, 1, 2, 0, 3, 0, 9, 0, 0],
                    [0, 0, 0, 0, 6, 9, 0, 4, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 7]])

Aug2021 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 9, 8, 5, 0, 0, 0, 2],
                    [0, 7, 0, 0, 3, 2, 0, 0, 6],
                    [0, 3, 0, 0, 0, 5, 9, 8, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 4, 8, 7, 0, 0, 0, 1, 0],
                    [5, 0, 0, 1, 4, 0, 0, 7, 0],
                    [2, 0, 0, 0, 6, 8, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]])

Sep2021 = np.array([[0, 0, 3, 0, 0, 0, 0, 0, 0],
                    [0, 0, 4, 0, 0, 5, 6, 0, 0],
                    [0, 7, 0, 9, 0, 0, 0, 2, 1],
                    [0, 9, 0, 5, 0, 6, 7, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 7, 3, 0, 4, 0, 8, 0],
                    [1, 8, 0, 0, 0, 2, 0, 3, 0],
                    [0, 0, 5, 6, 0, 0, 9, 0, 0],
                    [0, 0, 0, 0, 0, 0, 4, 0, 0]])

Oct2021 = np.array([[0, 0, 0, 0, 0, 7, 0, 0, 0],
                    [0, 0, 0, 8, 9, 0, 3, 0, 0],
                    [0, 3, 4, 0, 0, 0, 5, 0, 0],
                    [1, 0, 0, 0, 0, 8, 0, 6, 0],
                    [0, 7, 0, 0, 1, 0, 0, 4, 0],
                    [0, 8, 0, 7, 0, 0, 0, 0, 2],
                    [0, 0, 5, 0, 0, 0, 8, 2, 0],
                    [0, 0, 9, 0, 2, 4, 0, 0, 0],
                    [0, 0, 0, 6, 0, 0, 0, 0, 0]])

Nov2021 = np.array([[1, 0, 0, 9, 0, 0, 0, 0, 4],
                    [0, 2, 0, 0, 8, 0, 0, 0, 9],
                    [0, 0, 3, 0, 0, 6, 0, 0, 8],
                    [0, 0, 0, 1, 0, 0, 3, 8, 5],
                    [0, 0, 0, 0, 2, 0, 0, 0, 0],
                    [5, 8, 1, 0, 0, 3, 0, 0, 0],
                    [4, 0, 0, 6, 0, 0, 1, 0, 0],
                    [8, 0, 0, 0, 3, 0, 0, 2, 0],
                    [6, 0, 0, 0, 0, 9, 0, 0, 3]])

Dec2021 = np.array([[1, 0, 0, 0, 0, 3, 0, 0, 9],
                    [0, 8, 0, 4, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 6, 0, 0, 0, 0],
                    [9, 0, 0, 0, 0, 5, 0, 3, 0],
                    [0, 0, 2, 0, 3, 0, 4, 0, 0],
                    [0, 6, 0, 1, 0, 0, 0, 0, 2],
                    [0, 0, 0, 0, 4, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 8, 0, 5, 0],
                    [2, 0, 0, 9, 0, 0, 0, 0, 7]])

Jan2022 = np.array([[6, 0, 1, 0, 0, 9, 0, 0, 7],
                    [0, 0, 0, 1, 0, 0, 9, 0, 0],
                    [0, 7, 0, 0, 2, 0, 0, 0, 8],
                    [5, 0, 0, 0, 0, 0, 0, 6, 0],
                    [0, 0, 3, 0, 1, 0, 4, 0, 0],
                    [0, 9, 0, 0, 0, 0, 0, 0, 3],
                    [4, 0, 0, 0, 5, 0, 0, 7, 0],
                    [0, 0, 5, 0, 0, 6, 0, 0, 0],
                    [3, 0, 0, 8, 0, 0, 2, 0, 1]])

Feb2022 = np.array([[0, 0, 5, 0, 0, 0, 6, 0, 0],
                    [0, 6, 0, 0, 0, 0, 0, 3, 0],
                    [1, 0, 0, 0, 4, 0, 0, 0, 8],
                    [0, 0, 0, 9, 0, 7, 0, 0, 0],
                    [0, 0, 7, 0, 2, 0, 5, 0, 0],
                    [0, 0, 0, 6, 0, 5, 0, 0, 0],
                    [4, 0, 0, 0, 8, 0, 0, 0, 3],
                    [0, 1, 0, 0, 0, 0, 0, 5, 0],
                    [0, 0, 3, 0, 0, 0, 2, 0, 0]])

Mar2022 = np.array([[0, 0, 0, 0, 0, 6, 3, 7, 0],
                    [0, 0, 4, 9, 0, 0, 1, 0, 0],
                    [7, 0, 0, 0, 0, 5, 0, 0, 0],
                    [6, 5, 0, 0, 0, 0, 0, 0, 0],
                    [9, 0, 7, 0, 3, 0, 6, 0, 5],
                    [0, 0, 0, 0, 0, 0, 0, 1, 8],
                    [0, 0, 0, 2, 0, 0, 0, 0, 4],
                    [0, 0, 9, 0, 0, 8, 5, 0, 0],
                    [0, 2, 5, 3, 0, 0, 0, 0, 0]])

Apr2022 = np.array([[6, 7, 0, 0, 0, 0, 0, 2, 8],
                    [3, 0, 0, 0, 0, 0, 0, 0, 7],
                    [0, 0, 0, 5, 0, 9, 0, 0, 0],
                    [0, 0, 8, 0, 0, 7, 5, 0, 0],
                    [0, 0, 3, 0, 4, 0, 1, 0, 0],
                    [0, 0, 2, 9, 0, 0, 6, 0, 0],
                    [0, 0, 0, 8, 0, 1, 0, 0, 0],
                    [5, 0, 0, 0, 0, 0, 0, 0, 1],
                    [8, 9, 0, 0, 0, 0, 0, 3, 5]])

May2022 = np.array([[0, 0, 5, 6, 7, 8, 0, 0, 0],
                    [0, 4, 0, 0, 0, 0, 9, 0, 0],
                    [3, 0, 0, 0, 0, 0, 6, 0, 0],
                    [2, 0, 0, 0, 0, 5, 0, 0, 0],
                    [1, 0, 0, 0, 4, 0, 0, 0, 6],
                    [0, 0, 0, 3, 0, 0, 0, 0, 7],
                    [0, 0, 7, 0, 0, 0, 0, 0, 1],
                    [0, 0, 4, 0, 0, 0, 0, 8, 0],
                    [0, 0, 0, 1, 6, 3, 7, 0, 0]])

Jun2022 = np.array([[0, 0, 0, 0, 5, 3, 6, 0, 0],
                    [0, 0, 0, 4, 0, 0, 0, 9, 0],
                    [1, 2, 3, 0, 0, 0, 0, 7, 0],
                    [0, 0, 0, 0, 0, 0, 0, 5, 0],
                    [0, 0, 7, 3, 9, 2, 8, 0, 0],
                    [0, 9, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 0, 0, 0, 0, 5, 4, 1],
                    [0, 6, 0, 0, 0, 4, 0, 0, 0],
                    [0, 0, 2, 8, 1, 0, 0, 0, 0]])

Jul2022 = np.array([[0, 0, 0, 6, 5, 4, 0, 0, 0],
                    [0, 0, 1, 0, 0, 8, 9, 0, 0],
                    [0, 5, 0, 0, 0, 0, 7, 4, 0],
                    [6, 0, 0, 0, 0, 0, 0, 2, 7],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [8, 9, 0, 0, 0, 0, 0, 0, 6],
                    [0, 4, 2, 0, 0, 0, 0, 1, 0],
                    [0, 0, 7, 4, 0, 0, 3, 0, 0],
                    [0, 0, 0, 2, 9, 6, 0, 0, 0]])

Aug2022 = np.array([[0, 0, 0, 7, 8, 1, 0, 0, 0],
                    [0, 0, 6, 0, 0, 0, 0, 0, 0],
                    [0, 0, 9, 0, 0, 0, 3, 7, 0],
                    [3, 0, 0, 1, 0, 7, 0, 0, 9],
                    [9, 0, 0, 0, 6, 0, 0, 0, 4],
                    [8, 0, 0, 9, 0, 3, 0, 0, 2],
                    [0, 1, 3, 0, 0, 0, 5, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 4, 1, 2, 0, 0, 0]])

# All puzzles
Pzzls = {"Empty puzzle": Pzzlxx,
         "Sudoku book, cover": Pzzl00,
         "Sudoku book, puzzle 91": Pzzl91,
         "Alverde magazine, Februar 2021": Feb2021,
         "Alverde magazine, March 2021": Mar2021,
         "Alverde magazine, April 2021": Apr2021,
         "Alverde magazine, May 2021": May2021,
         "Alverde magazine, June 2021": Jun2021,
         "Alverde magazine, July 2021": Jul2021,
         "Alverde magazine, August 2021": Aug2021,
         "Alverde magazine, September 2021": Sep2021,
         "Alverde magazine, October 2021": Oct2021,
         "Alverde magazine, November 2021": Nov2021,
         "Alverde magazine, December 2021": Dec2021,
         "Alverde magazine, January 2022": Jan2022,
         "Alverde magazine, February 2022": Feb2022,
         "Alverde magazine, March 2022": Mar2022,
         "Alverde magazine, April 2022": Apr2022,
         "Alverde magazine, May 2022": May2022,
         "Alverde magazine, June 2022": Jun2022,
         "Alverde magazine, July 2022": Jul2022,
         "Alverde magazine, August 2022": Aug2022}


def solve(Pzzl, a):
    # find the first empty square
    for x in range(9):
        for y in range(9):
            if Pzzl[y][x]:
                # This is the last square, and it is not empty. We are done!
                if (x, y) == (8, 8):
                    return (True, a)
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

                # Can we solve the puzzle with the current cipher added?
                (scss, a) = solve(Pzzl, a)

                if scss:
                    # Yes, we solved it!
                    return (True, a)
                # No, that did not work. Try the next cipher.

            # No valid cipher found for the current square. Reset to zero and
            # backtrack!
            Pzzl[y][x] = 0
            a += 1
            return (False, a)


# Solve all puzzles in the dictionary P
def solvepuzzles(P):
    for k in P:
        Puzzle = P[k]
        print(k)
        print(Puzzle)
        print()

        (success, attempts) = solve(Puzzle, 0)

        if success:
            print(Puzzle)
            print("Attempts: {}\n\n".format(attempts))
        else:
            print("No solution found!")


# Main
if __name__ == '__main__':
    # Solve all puzzles (takes time!) or only the last one?
    c = input("Solve all (y/n)? ")

    # If yes, hand entire dictionary to iterating wrapper
    if c == 'y' or c == 'Y':
        solvepuzzles(Pzzls)

    # If no, hand a dictionary with only the last puzzle to iterating wrapper
    else:
        key = dict.keys()[-1]
        solvepuzzles({key: Pzzls[key]})
