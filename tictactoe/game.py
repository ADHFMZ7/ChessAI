
class Game:
  
  def __init__(self, size):
    
    self.board = [[0] * size for i in range(size)] 
    
    self.rows = [0] * size
    self.columns = [0] * size
    self.diag = [0] * 2

  # Checks if any win conditions are met
  # returns 1 if x wins, -1 if y wins, 0 if no one won
  def compute_win(self):
    if 3 in self.rows or 3 in self.columns or 3 in self.diag:
      return 1
    elif -3 in self.rows or -3 in self.columns or -3 in self.diag:
      return -1
    else:
      return 0
  
  # Takes a turn
  # Takes x, y coord and player
  # -1 for y, 1 for x
  def turn(self, coord, player):
    x, y = coord

    if ( 
        player not in [-1, 1] or
        x not in range(0, len(self.board)) or
        y not in range(0, len(self.board)) or
        self.board[x][y] != 0
       ):
      print("it was false")
      return False 
    else:
      print("turn valid")
      self.board[x][y] = player
      if x == y:
        self.diag[0] += player
      if x + y == len(self.board) - 1:
        self.diag[1] += player
      self.rows[x] += player
      self.columns[y] += player
      return True 



