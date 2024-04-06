'''
Created on 15.02.2021

__updated__='2024-04-06'

@author: jung
'''

import numpy as np

# Empty Puzzle
Pzzl_xx = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Puzzle from cover of Sudoku
Pzzl_00 = np.array([[0, 0, 0, 0, 8, 0, 9, 0, 0],
                    [4, 0, 2, 3, 0, 0, 6, 0, 0],
                    [9, 0, 1, 5, 0, 0, 0, 0, 3],
                    [0, 0, 4, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 6, 7, 8, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [1, 0, 0, 0, 0, 6, 2, 0, 7],
                    [0, 0, 9, 0, 0, 1, 3, 0, 5],
                    [0, 0, 3, 0, 4, 0, 0, 0, 0]])

# Puzzle number 91 from Sudoku book
Pzzl_91 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
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

Sep2022 = np.array([[0, 0, 0, 0, 2, 1, 0, 0, 0],
                    [0, 0, 0, 3, 0, 0, 0, 0, 0],
                    [0, 0, 4, 0, 0, 0, 7, 9, 3],
                    [0, 5, 0, 0, 0, 6, 0, 0, 1],
                    [6, 0, 0, 0, 7, 0, 0, 0, 9],
                    [7, 0, 0, 8, 0, 0, 0, 2, 0],
                    [8, 9, 3, 0, 0, 0, 5, 0, 0],
                    [0, 0, 0, 0, 0, 3, 0, 0, 0],
                    [0, 0, 0, 6, 1, 0, 0, 0, 0]])

Oct2022 = np.array([[0, 0, 4, 9, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 5, 7, 4, 0, 0],
                    [0, 8, 0, 0, 0, 0, 0, 0, 5],
                    [0, 9, 0, 0, 0, 0, 0, 0, 3],
                    [8, 3, 0, 0, 0, 0, 0, 2, 7],
                    [2, 0, 0, 0, 0, 0, 0, 8, 0],
                    [7, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 6, 5, 3, 0, 0, 0, 0],
                    [0, 0, 0, 0, 9, 1, 5, 0, 0]])

Nov2022 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [6, 0, 3, 0, 0, 0, 1, 0, 4],
                    [0, 2, 0, 5, 0, 1, 0, 7, 0],
                    [0, 0, 8, 0, 0, 0, 9, 0, 0],
                    [0, 0, 0, 7, 8, 3, 0, 0, 0],
                    [0, 0, 2, 0, 0, 0, 5, 0, 0],
                    [0, 6, 0, 9, 0, 5, 0, 1, 0],
                    [7, 0, 5, 0, 0, 0, 3, 0, 6],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]])

Dec2022 = np.array([[0, 1, 0, 0, 8, 0, 0, 0, 0],
                    [0, 0, 7, 4, 0, 0, 0, 0, 8],
                    [0, 0, 2, 5, 0, 0, 4, 7, 0],
                    [1, 0, 0, 0, 0, 0, 3, 2, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 6],
                    [0, 6, 8, 0, 0, 0, 0, 0, 0],
                    [0, 2, 9, 0, 0, 1, 7, 0, 0],
                    [3, 0, 0, 0, 0, 4, 9, 0, 0],
                    [0, 0, 0, 0, 6, 0, 0, 5, 0]])

Jan2023 = np.array([[0, 0, 5, 0, 0, 0, 9, 0, 0],
                    [0, 7, 0, 0, 0, 2, 0, 0, 4],
                    [0, 0, 2, 0, 6, 0, 0, 1, 0],
                    [5, 0, 0, 3, 0, 0, 8, 0, 0],
                    [0, 9, 0, 0, 1, 0, 0, 6, 0],
                    [0, 0, 3, 0, 0, 8, 0, 0, 7],
                    [0, 6, 0, 0, 9, 0, 1, 0, 0],
                    [8, 0, 0, 7, 0, 0, 0, 2, 0],
                    [0, 0, 4, 0, 0, 0, 5, 0, 0]])

Feb2023 = np.array([[0, 0, 0, 2, 0, 7, 6, 0, 0],
                    [0, 0, 7, 0, 0, 0, 3, 0, 0],
                    [3, 6, 0, 4, 0, 0, 0, 1, 7],
                    [4, 0, 1, 0, 0, 0, 5, 0, 6],
                    [0, 0, 0, 0, 2, 0, 0, 0, 0],
                    [6, 0, 8, 0, 0, 0, 1, 0, 2],
                    [7, 1, 0, 0, 0, 5, 0, 6, 3],
                    [0, 0, 6, 0, 0, 0, 9, 0, 0],
                    [0, 0, 4, 8, 0, 6, 0, 0, 0]])

Mar2023 = np.array([[0, 0, 0, 5, 6, 0, 0, 0, 0],
                    [0, 5, 0, 0, 0, 0, 9, 1, 0],
                    [0, 7, 0, 8, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 4, 0, 8],
                    [4, 0, 0, 0, 3, 0, 0, 0, 7],
                    [2, 0, 8, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 3, 0, 2, 0],
                    [0, 9, 7, 0, 0, 0, 0, 5, 0],
                    [0, 0, 0, 0, 7, 9, 0, 0, 0]])

Apr2023 = np.array([[8, 0, 0, 0, 0, 0, 0, 5, 6],
                    [2, 0, 0, 0, 0, 6, 0, 0, 0],
                    [0, 0, 0, 0, 2, 3, 0, 0, 0],
                    [0, 3, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 7, 0, 4, 0, 3, 0, 0],
                    [0, 0, 0, 0, 0, 0, 7, 2, 0],
                    [0, 0, 0, 8, 3, 0, 0, 0, 0],
                    [0, 0, 0, 9, 0, 0, 0, 0, 1],
                    [4, 6, 0, 0, 0, 0, 0, 0, 5]])

May2023 = np.array([[1, 0, 0, 0, 0, 0, 8, 0, 3],
                    [0, 2, 0, 3, 0, 0, 0, 0, 0],
                    [0, 0, 3, 0, 4, 0, 5, 0, 1],
                    [0, 3, 0, 4, 0, 0, 0, 0, 0],
                    [0, 0, 4, 0, 5, 0, 6, 0, 0],
                    [0, 0, 0, 0, 0, 6, 0, 7, 0],
                    [9, 0, 5, 0, 6, 0, 7, 0, 0],
                    [0, 0, 0, 0, 0, 7, 0, 8, 0],
                    [2, 0, 6, 0, 0, 0, 0, 0, 9]])

Jun2023 = np.array([[0, 0, 0, 1, 2, 3, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 5, 0, 0],
                    [8, 0, 0, 0, 0, 0, 0, 0, 3],
                    [0, 1, 0, 0, 0, 0, 0, 4, 0],
                    [0, 9, 0, 8, 6, 4, 0, 5, 0],
                    [0, 2, 0, 0, 0, 0, 0, 9, 0],
                    [5, 0, 0, 0, 0, 0, 0, 0, 9],
                    [0, 0, 3, 0, 0, 0, 4, 0, 0],
                    [0, 0, 0, 7, 8, 9, 0, 0, 0]])

Jul2023 = np.array([[8, 0, 0, 0, 0, 7, 0, 0, 3],
                    [0, 0, 6, 0, 0, 0, 1, 0, 0],
                    [0, 9, 0, 0, 2, 0, 0, 5, 0],
                    [0, 0, 0, 8, 0, 0, 0, 0, 9],
                    [0, 0, 1, 0, 7, 0, 2, 0, 0],
                    [3, 0, 0, 0, 0, 5, 0, 0, 0],
                    [0, 5, 0, 0, 9, 0, 0, 3, 0],
                    [0, 0, 7, 0, 0, 0, 8, 0, 0],
                    [1, 0, 0, 4, 0, 0, 0, 0, 6]])

Aug2023 = np.array([[0, 0, 6, 0, 0, 0, 0, 7, 0],
                    [0, 0, 0, 0, 0, 5, 0, 0, 4],
                    [9, 0, 5, 0, 0, 4, 8, 0, 0],
                    [0, 0, 0, 0, 0, 9, 2, 3, 0],
                    [0, 0, 0, 0, 8, 0, 0, 0, 0],
                    [0, 5, 8, 7, 0, 0, 0, 0, 0],
                    [0, 0, 7, 6, 0, 0, 9, 0, 2],
                    [3, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0, 5, 0, 0]])

Sep2023 = np.array([[0, 0, 0, 0, 0, 0, 8, 5, 0],
                    [1, 4, 0, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 7, 3, 0, 0, 0],
                    [0, 0, 5, 3, 0, 7, 0, 0, 0],
                    [0, 0, 3, 0, 9, 0, 2, 0, 0],
                    [0, 0, 0, 2, 0, 5, 3, 0, 0],
                    [0, 0, 0, 1, 3, 0, 0, 0, 2],
                    [0, 8, 0, 0, 0, 0, 0, 9, 4],
                    [0, 9, 6, 0, 0, 0, 0, 0, 0]])

Oct2023 = np.array([[0, 1, 8, 7, 0, 0, 0, 0, 0],
                    [0, 2, 0, 6, 0, 0, 4, 8, 5],
                    [0, 3, 4, 5, 0, 0, 7, 0, 2],
                    [0, 0, 0, 0, 0, 0, 6, 3, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 8, 5, 0, 0, 0, 0, 0, 0],
                    [2, 0, 7, 0, 0, 3, 1, 4, 0],
                    [3, 4, 6, 0, 0, 8, 0, 7, 0],
                    [0, 0, 0, 0, 0, 2, 5, 6, 0]])

Nov2023 = np.array([[0, 0, 7, 0, 0, 0, 8, 0, 0],
                    [0, 5, 0, 0, 2, 0, 0, 9, 0],
                    [9, 0, 3, 0, 0, 0, 7, 0, 1],
                    [0, 0, 0, 4, 0, 8, 0, 0, 0],
                    [0, 3, 0, 0, 0, 0, 0, 6, 0],
                    [0, 0, 0, 7, 0, 5, 0, 0, 0],
                    [4, 0, 9, 0, 0, 0, 3, 0, 5],
                    [0, 2, 0, 0, 8, 0, 0, 7, 0],
                    [0, 0, 1, 0, 0, 0, 4, 0, 0]])

Dec2023 = np.array([[0, 1, 0, 7, 0, 3, 0, 5, 0],
                    [0, 0, 7, 0, 0, 0, 8, 0, 0],
                    [0, 8, 0, 0, 0, 0, 0, 6, 0],
                    [7, 0, 0, 0, 5, 0, 0, 0, 6],
                    [0, 0, 0, 4, 0, 9, 0, 0, 0],
                    [9, 0, 0, 0, 6, 0, 0, 0, 2],
                    [0, 3, 0, 0, 0, 0, 0, 8, 0],
                    [0, 0, 5, 0, 0, 0, 6, 0, 0],
                    [0, 4, 0, 1, 0, 5, 0, 9, 0]])

Jan2024 = np.array([[0, 5, 6, 0, 0, 0, 4, 8, 0],
                    [1, 0, 0, 3, 0, 8, 0, 0, 5],
                    [9, 0, 0, 0, 7, 0, 0, 0, 2],
                    [0, 2, 0, 0, 0, 0, 0, 5, 0],
                    [0, 0, 9, 0, 1, 0, 8, 0, 0],
                    [0, 8, 0, 0, 0, 0, 0, 3, 0],
                    [7, 0, 0, 0, 8, 0, 0, 0, 4],
                    [8, 0, 0, 5, 0, 2, 0, 0, 3],
                    [0, 1, 5, 0, 0, 0, 9, 6, 0]])

Feb2024 = np.array([[0, 4, 0, 2, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 3, 0, 6],
                    [0, 8, 0, 4, 0, 3, 0, 5, 0],
                    [0, 0, 9, 0, 0, 0, 8, 0, 5],
                    [0, 0, 0, 0, 2, 0, 0, 0, 0],
                    [6, 0, 4, 0, 0, 0, 7, 0, 0],
                    [0, 6, 0, 1, 0, 5, 0, 7, 0],
                    [3, 0, 8, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 9, 0, 2, 0]])

Mar2024 = np.array([[9, 0, 0, 3, 0, 0, 0, 1, 5],
                    [4, 0, 0, 9, 0, 7, 0, 0, 0],
                    [0, 0, 0, 0, 0, 6, 0, 0, 0],
                    [0, 7, 1, 0, 0, 0, 0, 5, 6],
                    [0, 0, 0, 0, 3, 0, 0, 0, 0],
                    [8, 9, 0, 0, 0, 0, 2, 7, 0],
                    [0, 0, 0, 2, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 4, 0, 0, 9],
                    [1, 6, 0, 0, 0, 3, 0, 0, 4]])

Apr2024 = np.array([[0, 0, 7, 2, 0, 5, 6, 0, 0],
                    [0, 0, 0, 3, 0, 4, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0, 0, 4],
                    [3, 4, 0, 0, 0, 0, 0, 9, 7],
                    [0, 0, 0, 0, 4, 0, 0, 0, 0],
                    [8, 9, 0, 0, 0, 0, 0, 1, 3],
                    [7, 0, 0, 0, 0, 0, 0, 0, 8],
                    [0, 0, 0, 1, 0, 9, 0, 0, 0],
                    [0, 0, 5, 6, 0, 7, 2, 0, 0]])

# All puzzles
Pzzls = {"Empty puzzle": Pzzl_xx,
         "Sudoku book, cover": Pzzl_00,
         "Sudoku book, puzzle 91": Pzzl_91,
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
         "Alverde magazine, August 2022": Aug2022,
         "Alverde magazine, September 2022": Sep2022,
         "Alverde magazine, October 2022": Oct2022,
         "Alverde magazine, November 2022": Nov2022,
         "Alverde magazine, December 2022": Dec2022,
         "Alverde magazine, January 2023": Jan2023,
         "Alverde magazine, February 2023": Feb2023,
         "Alverde magazine, March 2023": Mar2023,
         "Alverde magazine, April 2023": Apr2023,
         "Alverde magazine, May 2023": May2023,
         "Alverde magazine, June 2023": Jun2023,
         "Alverde magazine, July 2023": Jul2023,
         "Alverde magazine, August 2023": Aug2023,
         "Alverde magazine, September 2023": Sep2023,
         "Alverde magazine, October 2023": Oct2023,
         "Alverde magazine, November 2023": Nov2023,
         "Alverde magazine, December 2023": Dec2023,
         "Alverde magazine, January 2024": Jan2024,
         "Alverde magazine, February 2024": Feb2024,
         "Alverde magazine, March 2024": Mar2024,
         "Alverde magazine, April 2024": Apr2024}


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
        solvepuzzles(dict([Pzzls.popitem()]))
