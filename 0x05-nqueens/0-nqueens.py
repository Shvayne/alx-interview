#!/usr/bin/python3
"""
    This script contains various fuctions that together, solves
    the N queens problem using backtracking.
"""

import sys

def is_safe(board, row, col):
    """
        checks if it is safe to place a queen at board[row][col].
        Ensures that no other queens are in the same row, upper
        diagonal or lower diagonal.

        parameters:
        board (list of list of int): The chessboard represented as a 2D list
        row (int): The row index to check.
        col: (int): The column index to check.

        Returns:
        boolean: True if it's safe to place the queen, False otherwise.
    """
    #check the current row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    #check Lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col, solutions):
    """
      Recursively attempts to place queens on the board, one column at
      a time. Collects all valid solutions where queens are non attacking

      parameter:
      board (list of list of int): The chessboard
      col (int): The current column index where a queen is to be placed
      solutions (list of list of list of int): COllects all solutions as lists
      of queen positions.
    """
    if col == len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solutions)
        return
    
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col+1, solutions)
            board[i][j] = 0


def main():
    """
      Main function to handle user input, validate it and start solving
      the N Queens puzzle.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()