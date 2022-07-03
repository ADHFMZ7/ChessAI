from game import Game

game = Game(3)

players = {
  -1 : 'y',
  0  : ' ',
  1  : 'x'
  }


while not game.compute_win():
  print("\n-------")
  for i in game.board:
      print('|', end='')
      for j in i:
        print(players[j], end='|')

      print("\n-------")
  coord = tuple(int(input()) for i in range(2)) 
  print(coord)
  game.turn(coord, int(input("Player(y: -1, x: 1): ")))
 
