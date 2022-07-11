from tkinter import *
from tkinter import font as font
from random import randint
from minimax import minimax

players = {
 -1: 'O',
  0: ' ',
  1: 'X'
}

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
    self.grid = self.valid_turns
    
    # initialize gui
    self.window = Tk()
    myFont = font.Font(size=50//self.size, weight='bold') 
    self.buttons = [[0] * size  for i in range(size)]
    for x, y in self.valid_turns:
      self.buttons[x][y] = Button(self.window, 
                                  command=lambda row=x, 
                                  column=y: self.on_click(row, column),
                                  width=18//self.size,
                                  height=21//self.size,
                                  font=myFont)
      
      self.buttons[x][y].grid(row=x, column=y) 
    
    self.window.mainloop() 

  def end_game(self):
    for x, y in self.grid:
      self.buttons[x][y].config(state='disabled')
    
  def on_click(self, x, y): 
    self.take_turn((x, y))
    if self.winner() or self.is_full():
      self.end_game()
    self.take_turn(self.ai_turn())
    if self.winner() or self.is_full():
      self.end_game() 
    
  
  
  # Checks if any win conditions are met
  # returns 1 if x wins, -1 if y wins, 0 if no one won
  def winner(self):
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
    
    self.buttons[x][y].config(text=players[self.board[x][y]], state='disabled')
    self.turn += 1
    return True 

  def ai_turn(self):
    #return (self.valid_turns[0] if len(self.valid_turns) == 1 else
    #        self.valid_turns[randint(0, len(self.valid_turns)-1)])
    return self.best_move()

  def best_move(self):
    scores = []
    max_index = 0
    for i in range(len(self.valid_turns)):
      scores.append(minimax(self, self.turn, -1))
      max_index = max(max_index, scores[i])
    return self.valid_turns[max_index]


  # returns True if Board is full
  # returns False otherwise
  def is_full(self):
    return len(self.valid_turns) == 0

if __name__ == "__main__":
  game = Game(3) 