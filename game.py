# Define a function to print the board
def print_board(board):
    print("  0 1 2")
    for i in range(3):
        row_str = str(i) + " "
        for j in range(3):
            if board[i][j] == -1:
                row_str += " "
            elif board[i][j] == 0:
                row_str += "O"
            else:
                row_str += "X"
            if j < 2:
                row_str += "|"
        print(row_str)
        if i < 2:
            print("  -----")

# Define a function to check if someone has won
def check_win(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    # Check columns
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Initialize the board
board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

# Define the players
players = {0: "O", 1: "X"}

# Define the current player
current_player = 0

# Print the board
print_board(board)

# Loop until someone wins or the board is full
while not check_win(board, 0) and not check_win(board, 1) and any(-1 in row for row in board):
    # Get the current player's move
    valid_move = False
    while not valid_move:
        move_str = input("Player " + players[current_player] + ", enter your move (row column): ")
        move = move_str.split()
        if len(move) != 2:
            print("Invalid move. Please enter your move in the format 'row column'.")
            continue
        try:
            row = int(move[0])
            col = int(move[1])
        except ValueError:
            print("Invalid move. Please enter your move as two integers separated by a space.")
            continue
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move. Please enter a row and column between 0 and 2.")
            continue
        if board[row][col] != -1:
            print("Invalid move. That spot is already taken.")
            continue
        valid_move = True
    # Update the board
    board[row][col] = current_player
    # Print the board
    print_board(board)
    # Switch to the other player
    current_player = (current_player + 1) % 2

# Check who won or if it was a tie
if check_win(board, 0):
    print("Player O wins!")
elif check_win(board, 1):
    print("Player X wins!")
else:
    print("Tie game.")
