# Authors: Yeo Yong Kiat & Lim Xuan Ping
# Date: 17 Jul 2018
# Definitions
# -This program has two objects:
#     1. Square = each individual square on the board, contains mines and values
#     2. Squares = an aggregator class for the squares on the board
# -State: whether each square is a mine or note
# -Revealed: whether each square has been revealed or not
# -Value: number of mines surrounding each square
# -This version of minesweeper does not have the "flag" function.

import random
import sys

## Defining a Square class to contain the mines and values... ##
class Square():
  def __init__(self, state, revealed, value, x, y):
    self.state = state
    self.revealed = revealed
    self.value = value
    self.x, self.y = x, y
  def render_square(self):
    if self.revealed:
        return str(self.value)
    else:
        return '-'

## Defining a Squares class as an aggregator of all the squares... ##
class Squares():
  board = []
  mines = []
  total_squares = 0
  total_mines = 0
  is_over = False
  def __init__(self, cols, rows):
      cols, rows = int(cols), int(rows)
      self.board = [[Square(False, False, 0, x, y) for x in range(cols)] for y in range(rows)]
      self.total_squares = cols * rows
      # set random mines into board
      self.__randomize_mines(cols, rows, self.board)

      # calculate value of each square
      self.__calculate_values(cols, rows, self.board)

  def print_mine_locations(self):
    n, m = len(self.board), len(self.board[0])

    for i in range(n):
      s = ''
      for j in range(m):
        s = s + 'M' if self.board[i][j].state else '-'
      print(s)

  def print_values(self):
    n, m = len(self.board), len(self.board[0])

    for i in range(n):
      s = ''
      for j in range(m):
        s = s + str(self.board[i][j].value)
      print(s)

  def reveal(self, x, y):
    board = self.board
    x, y = int(x), int(y)
    # check row
    if y >= len(board) or y < 0:
      print('Please enter a value between ',0,' and ',len(board)-1)
      return
    # check col
    if x >= len(board[0]) or x < 0:
      print('Please enter a value between ',0,' and ',len(board[0])-1)
      return
    if self.board[y][x].state: self.game_over()
    else:
      self.board[y][x].revealed = True
      if self.board[y][x].value == 0:
        self.__expand_blank(x, y, self.board)

  def game_over(self):
    print("Bwahahaha, you have died. Try again if you want.")
    self.is_over = True

  def __expand_blank(self, x, y, board):
    deltas = [
      (-1,  -1), (0,   1), (1,   1),
      (-1,   0),           (1,   0),
      (-1,   1), (0,  -1), (1,  -1),
    ]
    queue = [board[y][x]]
    # check if each square is blank
    if board[y][x].value == 0:
      while queue:
        square = queue.pop(0)
        x,y = square.x, square.y
        # check if surrounding squares are blank
        for delta in deltas:
          dx, dy = x+delta[0], y+delta[1]
          if self.__is_within_range(dx, dy) and\
             not board[dy][dx].revealed:

            # check if not bomb
            if not board[dy][dx].state:
              board[dy][dx].revealed = True
              #  check if value zero
              if board[dy][dx].value == 0:
                queue.append(board[dy][dx])


  def __randomize_mines(self, cols, rows, board):
    # the squares:mines ratio is fixed to 25% here...
    self.total_mines = int(self.total_squares/4)
    # self.total_mines = 4
    remaining_mines = self.total_mines
    xrange, yrange = range(cols),range(rows)

    while remaining_mines > 0:
      x,y = random.choice(xrange),random.choice(yrange)

      if not board[x][y].state:
        self.mines.append(board[x][y])
        board[x][y].state = True
        remaining_mines = remaining_mines - 1

  def __calculate_values(self, cols, rows, board):

    deltas = [
      (-1,  -1), (0,   1), (1,   1),
      (-1,   0),           (1,   0),
      (-1,   1), (0,  -1), (1,  -1),
    ]
    # intead of checking all the corners, loop through mines and deltas
    # and increment the values surrounding mine
    for mine in self.mines:
      for delta in deltas:
        y, x = mine.y+delta[1], mine.x+delta[0]
        if self.__is_within_range(x, y):
          board[y][x].value += 1

  def __is_within_range(self, x, y):
    board = self.board
    width, length = len(board[0]), len(board)
    return x >= 0 and x < width and y >= 0 and y < length

## Defining a function to print out the board on the commandline interface... ##
def print_board(board):
  n, m = len(board), len(board[0])
  for i in range(n):
    s = ''
    for j in range(m):
      s = s + board[i][j].render_square()
    print(s)

## Game starts here... ##
print('specify the size of your minesweeper board:')
cols = input('number of columns:')
rows = input('number of rows:')
game = Squares(int(cols), int(rows))
print_board(game.board)
print('Welcome to the minesweeper game.\nEnter x and y coordinates to reveal!')
while True:
  print("x and y are zero based because I don't know how to shift the index :p")
  print("zero based means instead of starting 1, it will start with 0")
  print("x = column index, y = row index")
  x = input('x:')
  y = input('y:')
  game.reveal(x,y)
  print_board(game.board)
  if game.is_over: break
