import math

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board():
    for row in board:
        print("|".join(row))
        print("-----")

def is_full():
    for row in board:
        if " " in row:
            return False
    return True

def is_winner(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def evaluate():
    if is_winner("X"):
        return 1
    elif is_winner("O"):
        return -1
    else:
        return 0

def minimax(depth, is_maximizing, alpha, beta):
    if is_winner("X"):
        return 1
    if is_winner("O"):
        return -1
    if is_full():
        return 0
    
    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move():
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval = minimax(0, False, -math.inf, math.inf)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def play_game():
    current_player = "O"
    while not is_full():
        print_board()
        
        if current_player == "O":
            print("Your turn (O):")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] != " ":
                print("Invalid move. Try again.")
                continue
        else:
            print("AI's turn (X):")
            move = find_best_move()
            row, col = move
            print(f"AI chooses: Row {row}, Column {col}")
        
        board[row][col] = current_player
        
        if is_winner(current_player):
            print_board()
            print(f"{current_player} wins!")
            return
        
        current_player = "X" if current_player == "O" else "O"
    
    print_board()
    print("It's a draw!")

play_game()
