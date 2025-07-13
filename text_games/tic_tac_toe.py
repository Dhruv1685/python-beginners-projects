# Tic Tac Toe Game
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
        except ValueError:
            print("❌ Invalid input. Please enter numbers 0, 1, or 2.")
            continue

        # Validating move
        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == " ":
                board[row][col] = current_player

                if check_winner(board, current_player):
                    print_board(board)
                    print(f"🎉 Player {current_player} wins!")
                    break
                elif is_full(board):
                    print_board(board)
                    print("🤝 It's a draw!")
                    break

                # Switch players
                current_player = "O" if current_player == "X" else "X"
            else:
                print("❗ Cell already taken. Try again.")
        else:
            print("❌ Invalid cell. Please choose row and column between 0 and 2.")

tic_tac_toe()
