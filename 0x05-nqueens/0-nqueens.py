#!/usr/bin/python3

import sys


def is_safe(board, row, col):
    """function that checks if it's safe to place a queen
    at a given row and column on the chessboard"""
    for i in range(row):
        """
        starting a loop that iterates through the rows
        of the board up to the current row
        """
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """
    solves the N-Queens problem for a given n.
    """
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    def backtrack(row, board):
        """
        a recursive function.
        takes in the current row and the current state of the board as args
        """
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board)

    solutions = []
    backtrack(0, [0] * n)

    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    solve_nqueens(n)
