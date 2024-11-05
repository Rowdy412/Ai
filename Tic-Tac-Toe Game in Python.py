# Tic-Tac-Toe Game in Python

def print_board(board):
    """Function to print the Tic-Tac-Toe board"""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    """Function to check if there is a winner"""
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]             # diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    """Function to check if the board is full"""
    return all(s != ' ' for s in board)

def play_game():
    """Main function to play the game"""
    board = [' '] * 9  # Tic-Tac-Toe board
    current_player = 'X'  # Starting player

    while True:
        print_board(board)
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        if board[move] != ' ':
            print("Invalid move! The cell is already taken. Try again.")
            continue

        board[move] = current_player

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
