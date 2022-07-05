from game import players, Game

SIZE = 10

def take_input():
  x, y = input("enter coordinates separated by a space: ").split(' ')
  return int(x), int(y) 

def print_board():
  print("\n", end='')
  print("-" * (SIZE * 2 + 1))
  for i in game.board:
      print('|', end='')
      for j in i:
        print(players[j], end='|')
      print("\n", end='')
      print("-" * (SIZE * 2 + 1))


if __name__ == "__main__":

  game = Game(SIZE)

  while not game.winner() and not game.is_full():
    
    print_board()
    game.take_turn(take_input())

  print_board()
  print(f"Player: {players[game.winner()]} has won")
