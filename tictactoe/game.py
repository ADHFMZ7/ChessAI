from random import randint

players = {
 -1: 'O',
  0: ' ',
  1: 'x'
}


class Game:
  
  def __init__(self, size):
   
    # store board information
    self.board = [[0] * size for i in range(size)] 
    self.size = size

    # used for calculating win
    self.rows = [0] * size
    self.columns = [0] * size
    self.diag = [0] * 2
    
    # used for ai turn pool
    self.turn = 0
    self.valid_turns = [(i, j) for i in range(size) for j in range(size)]


  # Checks if any win conditions are met
  # returns 1 if x wins, -1 if y wins, 0 if no one won
  def winner(self):
    self.print_board()
    if self.size in self.rows + self.columns + self.diag:
      print(f"{players[1]} has won!")
      return 1
    elif -self.size in self.rows + self.columns + self.diag:
      print(f"{players[-1]} has won!")
      return -1
    else:
      if self.is_full():
        print("Draw!")
      return 0


  # Takes a turn
  # Takes x, y coord as tuple
  # -1 for y, 1 for x
  def take_turn(self, coord):
    x, y = coord
    if (x, y) not in self.valid_turns:
      return False 
    else:
      player = -1 if self.turn % 2 else 1
      self.board[x][y] = player
      self.valid_turns.remove((x, y))
      if x == y:
        self.diag[0] += player
      if x + y == len(self.board) - 1:
        self.diag[1] += player
      self.rows[x] += player
      self.columns[y] += player
      self.turn += 1
      return True 

  def ai_turn(self):
    return self.valid_turns[randint(0, len(self.valid_turns)-1)] 


  # returns True if Board is full
  # returns False otherwise
  def is_full(self):
    return len(self.valid_turns) == 0

  def take_input(self):
    try:
      x, y = input("enter coordinates separated by space: ").split() 
    except ValueError:
      print("invalid number, try again")
      return self.take_input() 
    return int(x), int(y)


  def print_board(self):
    print("\n", end='')
    print("-" * (self.size * 2 + 1))
    for i in self.board:
        print('|', end='')
        for j in i:
          print(players[j], end='|')
        print("\n", end='')
        print("-" * (self.size * 2 + 1))
