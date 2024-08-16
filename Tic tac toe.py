def print_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|   " + row[0] + "   |   " + row[1] + "   |   " + row[2] + "   |")
        print("+-------+-------+-------+")

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def get_user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Try again.")
            else:
                row, col = divmod(move - 1, 3)
                if board[row][col] in ['O', 'X']:
                    print("Cell already taken. Try again.")
                else:
                    return row, col
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

def get_computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] not in ['O', 'X']]
    if empty_cells:
        return empty_cells[0]

def play_game():
    board = [[str(i + 1) for i in range(3)] for j in range(3)]
    board[1][1] = 'X'
    print_board(board)

    while True:
        row, col = get_user_move(board)
        board[row][col] = 'O'
        print_board(board)

        if check_win(board, 'O'):
            print("You won!")
            break
        if all(cell in ['O', 'X'] for row in board for cell in row):
            print("It's a tie!")
            break

        row, col = get_computer_move(board)
        board[row][col] = 'X'
        print("Computer chose cell", row * 3 + col + 1)
        print_board(board)

        if check_win(board, 'X'):
            print("Computer won!")
            break

    print("Game over")

def main():
    print("hello")
    while True:
        play_game()
        replay = input("Do you want to play again? (yes/no): ")
        if replay.lower() != 'yes':
            print("Thanks for playing!")
            break

main()
