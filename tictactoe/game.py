from random import randint
from copy import deepcopy
from minimax import minimax

players = {
 -1: 'O',
  0: ' ',
  1: 'X'
}

AI = -1

class Game:
  
  def __init__(self, size):
   
    # store board information
    self.board = [[0] * size for i in range(size)] 
    self.size = size

    # used for calculating win
    self.rows    = [0] * size
    self.columns = [0] * size
    self.diag    = [0] * 2
    
    # used for ai turn pool
    self.turn = 0
    self.valid_turns = [(i, j) for i in range(size) for j in range(size)]


  
  def ai_turn(self):
    if self.turn == 0: 
      return (self.valid_turns[0] if len(self.valid_turns) == 1 else
              self.valid_turnss[randint(0, len(self.valid_turns)-1)])
    return self.best_move()

  
  # def best_move(self):
  #   scores = []
  #   min_index = 0
  #   for i in range(len(self.valid_turns)):
  #     temp = deepcopy(self)
  #     temp.take_turn(self.valid_turns[i])
  #     scores.append(minimax(temp, (self.size**2)-self.turn, AI))
  #     min_index = i if scores[i] < scores[min_index] else min_index
  #   print(self.valid_turns)
  #   print(scores)
  #   print("min: ", min_index)
  #   return self.valid_turns[min_index]


# Checks if any win conditions are met
  # returns 1 if x wins, -1 if y wins, 0 if no one won
  def winner(self):
  
    if self.size in self.rows + self.columns + self.diag:
      # print(f"{players[1]} has won!")
      return 1
    elif -self.size in self.rows + self.columns + self.diag:
      # print(f"{players[-1]} has won!")
      return -1
    else:
      if self.is_full():
        # print("Draw!")
        pass
      return 0

  # Takes a turn
  # Takes x, y coord as tuple
  # -1 for y, 1 for x
  def take_turn(self, coord):
    x, y = coord
    player = -1 if self.turn % 2 else 1
    self.board[x][y] = player
    self.valid_turns.remove((x, y))
   
    # updates score
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
    return len(self.valid_turns) == 0


  # Takes input and makes sure it is valid
  def take_input(self):
    try:
      x, y = input("enter coordinates separated by space: ").split() 
      x, y = int(x), int(y)
    except ValueError:
      print("invalid number, try again")
      return self.take_input() 
    
    if ( x not in range(0, self.size) or 
         y not in range(0, self.size) or
         (x, y) not in self.valid_turns):
      print("number not in range, try again")
      return self.take_input()
    return x, y


  def __str__(self):
    res = "\n"+"-" * (self.size * 2 + 1) + '\n'
    for i in self.board:
        res += '|'
        for j in i:
          res += f"{players[j]}|"
        res+="\n"+"-" * (self.size * 2 + 1) + '\n'
    return res
  
class HumanPlayer:
  def__init__(self, game, player):
    self.game = game  
    self.player = player
  
  def take_turn():