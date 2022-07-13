from game import players, Game
from minimax import minimax

SIZE = 4

if __name__ == "__main__":

  game = Game(SIZE)
  # game.take_turn((0, 2))
  # game.take_turn((0, 0))
  # game.take_turn((1, 1))
  # game.take_turn((2, 0))
  # game.take_turn((1, 0))
 
  print(game)
  while not game.winner() and not game.is_full():
    if game.turn % 2:  
      game.take_turn(game.ai_turn()) 
      print(game)
    else: 
      game.take_turn(game.take_input())
      print(game)
  print(f"{players[game.winner()]} has Won") if game.winner() else print("Draw!")
  

    