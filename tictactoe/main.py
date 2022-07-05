from game import players, Game

SIZE = 3

if __name__ == "__main__":

  game = Game(SIZE)

  while not game.winner() and not game.is_full():
    game.take_turn(game.take_input())
    game.take_turn(game.ai_turn())
