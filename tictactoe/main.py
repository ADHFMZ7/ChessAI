from game import Game

game = Game(3)

while game.compute_win != 1 or game.compute_win != -1:
     
    for i in game.board:
      print(i)
    print(game.compute_win())
