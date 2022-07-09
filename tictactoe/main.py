from game import players, Game

SIZE = 13 

if __name__ == "__main__":

  game = Game(SIZE)
 
  while not game.winner() and not game.is_full():
    if not game.turn % 2:
      game.take_turn(game.take_input()) 
    else: 
      game.take_turn(game.ai_turn())
