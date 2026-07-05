import math

board = [' ' for _ in range(9)]


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def print_positions():
    print()
    print("Board Positions:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")
    print()


def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_draw():
    return ' ' not in board


def minimax(is_max):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = "O"
                score = minimax(False)
                board[i] = ' '
                best = max(best, score)

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = "X"
                score = minimax(True)
                board[i] = ' '
                best = min(best, score)

        return best


def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = "O"
            score = minimax(False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"


def human_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): "))

            if pos < 1 or pos > 9:
                print("Choose between 1 and 9.")
                continue

            if board[pos-1] != ' ':
                print("Position already occupied.")
                continue

            board[pos-1] = "X"
            break

        except ValueError:
            print("Invalid input.")


print("=" * 40)
print(" TIC TAC TOE AI ")
print("=" * 40)

print_positions()

while True:

    print_board()

    human_move()

    if check_winner("X"):
        print_board()
        print("🎉 You Win!")
        break

    if is_draw():
        print_board()
        print("Game Draw!")
        break

    print("AI is thinking...")

    ai_move()

    if check_winner("O"):
        print_board()
        print("🤖 AI Wins!")
        break

    if is_draw():
        print_board()
        print("Game Draw!")
        break