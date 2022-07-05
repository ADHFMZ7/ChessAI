
players = {
 -1: 'y',
  0: ' ',
  1: 'x'
}


class Game:
  
  def __init__(self, size):
    
    self.board = [[0] * size for i in range(size)] 
    self.size = size
    self.rows = [0] * size
    self.columns = [0] * size
    self.diag = [0] * 2
    self.turn = 0

  # Checks if any win conditions are met
  # returns 1 if x wins, -1 if y wins, 0 if no one won
  def winner(self):
    if self.size in self.rows or self.size in self.columns or self.size in self.diag:
      return 1
    elif -self.size in self.rows or -self.size in self.columns or -self.size in self.diag:
      return -1
    else:
      return 0


  # Takes a turn
  # Takes x, y coord and player
  # -1 for y, 1 for x
  def take_turn(self, coord):
    x, y = coord
    if ( 
        x not in range(0, len(self.board)) or
        y not in range(0, len(self.board)) or
        self.board[x][y] != 0
       ):
      return False 
    else:
      player = -1 if self.turn % 2 else 1
      self.board[x][y] = player
      if x == y:
        self.diag[0] += player
      if x + y == len(self.board) - 1:
        self.diag[1] += player
      self.rows[x] += player
      self.columns[y] += player
      self.turn += 1
      return True 

  # returns True if Board is full
  # returns False otherwise
  def is_full(self):
    for i in self.board:
      for j in i:
        if j == 0:
          return False
    return True
