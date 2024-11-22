  #!/usr/bin/python3
  """N Queens puzzle solution"""
  import sys


  def print_board(board):
      """Prints the coordinates of queens on the board"""
      queens = []
      for i in range(len(board)):
          for j in range(len(board)):
              if board[i][j] == 1:
                  queens.append([i, j])
      print(queens)


  def is_safe(board, row, col, n):
      """Checks if a queen can be placed on board[row][col]"""
      # Check row on left side
      for j in range(col):
          if board[row][j]:
              return False

      # Check upper diagonal on left side
      i, j = row, col
      while i >= 0 and j >= 0:
          if board[i][j]:
              return False
          i -= 1
          j -= 1

      # Check lower diagonal on left side
      i, j = row, col
      while i < n and j >= 0:
          if board[i][j]:
              return False
          i += 1
          j -= 1

      return True


  def solve_nqueens(board, col, n):
      """Recursive function to solve N Queens problem"""
      if col >= n:
          print_board(board)
          return True

      res = False
      for i in range(n):
          if is_safe(board, i, col, n):
              board[i][col] = 1
              solve_nqueens(board, col + 1, n)
              board[i][col] = 0
      return False


  def main():
      """Main function to handle input and start solution"""
      if len(sys.argv) != 2:
          print("Usage: nqueens N")
          sys.exit(1)

      try:
          n = int(sys.argv[1])
      except ValueError:
          print("N must be a number")
          sys.exit(1)

      if n < 4:
          print("N must be at least 4")
          sys.exit(1)

      board = [[0 for x in range(n)] for y in range(n)]
      solve_nqueens(board, 0, n)


  if __name__ == "__main__":
      main()
