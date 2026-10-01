# Initialize the board with numbers 1 to 9
board = [" " for _ in range(9)]


def print_board():
  print()
  print(f" {board[0]} | {board[1]} | {board[2]} ")
  print("---|---|---")
  print(f" {board[3]} | {board[4]} | {board[5]} ")
  print("---|---|---")
  print(f" {board[6]} | {board[7]} | {board[8]} ")
  print()


def check_win(player):
  # Winning combinations: rows, columns, diagonals
  win_conditions = [
      (0, 1, 2),
      (3, 4, 5),
      (6, 7, 8),  # Rows
      (0, 3, 6),
      (1, 4, 7),
      (2, 5, 8),  # Columns
      (0, 4, 8),
      (2, 4, 6),  # Diagonals
  ]
  return any(
      board[c1] == board[c2] == board[c3] == player for c1, c2, c3 in win_conditions
  )                                                                                               


def check_tie():
  return " " not in board


def play_game():
  current_player = "X"
  print("Welcome to Tic-Tac-Toe!")

  while True:
    print_board()
    print(f"Player {current_player}'s turn.")

    try:
      choice = int(input("Choose a position (1-9): ")) - 1
      if choice < 0 or choice > 8 or board[choice] != " ":
        print("Invalid move. Try an empty spot between 1 and 9.")
        continue
    except ValueError:
      print("Please enter a valid number from 1 to 9.")
      continue

    board[choice] = current_player

    if check_win(current_player):
      print_board()
      print(f"Player {current_player} wins!")
      break

    if check_tie():
      print_board()
      print("It's a tie!")
      break

    # Switch player
    current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
  play_game()
