from random import randrange


def display_board(board):
    print()
    print(board[0][0], '|', board[0][1], '|', board[0][2])
    print('---------')
    print(board[1][0], '|', board[1][1], '|', board[1][2])
    print('---------')
    print(board[2][0], '|', board[2][1], '|', board[2][2])
    print()


def enter_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if not move.isdigit():
            print("Please enter a number.")
            continue

        move = int(move)
        if move < 1 or move > 9:
            print("The number must be between 1 and 9.")
            continue

        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] == 'O' or board[row][col] == 'X':
            print("That square is already taken. Try again.")
            continue

        board[row][col] = 'O'
        return


def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != 'O' and board[row][col] != 'X':
                free_fields.append((row, col))
    return free_fields


def victory_for(board, sign):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True

    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    row, col = free_fields[randrange(len(free_fields))]
    board[row][col] = 'X'


def main():
    board = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print("Let's play tic-tac-toe!")
    print("The computer plays X, you play O.")

    board[1][1] = 'X'
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)

        if victory_for(board, 'O'):
            print("You win! Congratulations!")
            break

        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

        draw_move(board)
        display_board(board)

        if victory_for(board, 'X'):
            print("The computer wins!")
            break

        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break


if __name__ == '__main__':
    main()
