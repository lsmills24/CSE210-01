# Tic-Tac-Toe 
# By: Loran Mills


def main():
    player = "x"
    board = create_board()
    while not (win(board) or tie(board)):
        display_board(board)
        take_turn(player, board)
        player = next_player(player)
    display_board(board)
    print("Great Game! Well Played!")


def create_board():
    board = []
    for i in range(9):
        board.append(i + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def win(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def tie(board):
    for i in range(9):
        if board[i] != "x" and board[i] != "o":
            return False
    return True

def take_turn(player, board):
   place = int(input(f"{player}'s turn to chose a space (1-9): "))
   board[place - 1] = player

def next_player(current_player):
    if current_player == "" or current_player == "x":
        return "o"
    elif current_player == "o":
        return "x"


if __name__ == "__main__":
    main()