from game import players, Game
from minimax import minimax

SIZE = 3

if __name__ == "__main__":

  game = Game(SIZE)
  print(game)
  while not game.winner() and not game.is_full():
    if game.turn % 2:  
      game.take_turn(game.ai_turn()) 
    else: 
      game.take_turn(game.take_input())
    print(minimax(game, game.turn, 1))
    print(minimax(game, game.turn, -1))

