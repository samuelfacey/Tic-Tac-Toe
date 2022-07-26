board = "      x\n  _ | _ | _\n  ---------\ny _ | _ | _\n  ---------\n  _ | _ | _"

backend_board = {
    "1,1": False,
    "1,2": False,
    "1,3": False,
    "2,1": False,
    "2,2": False,
    "2,3": False,
    "3,1": False,
    "3,2": False,
    "3,3": False,
}

hand = {
    "1,1": 10,
    "1,2": 14,
    "1,3": 18,
    "2,1": 34,
    "2,2": 38,
    "2,3": 42,
    "3,1": 58,
    "3,2": 62,
    "3,3": 66,
}

print(board)
is_running = True
board_list = []

for char in board:
    board_list.append(char)


def player_one():
    is_playing = True
    while is_playing == True:
        move = input("\nPlayer X, Where would you like to place your move?")
        if backend_board[move] != True:
            backend_board[move] = True
            draw = hand[move]
            board_list[draw] = "X"
            print("".join(board_list))
            is_playing = False
        else:
            print("\nThere's already a mark there! Try again.")


def player_two():
    is_playing = True
    while is_playing == True:
        move = input("\nPlayer 0, Where would you like to place your move?")
        if backend_board[move] != True:
            backend_board[move] = True
            draw = hand[move]
            board_list[draw] = "0"
            print("".join(board_list))
            is_playing = False
        else:
            print("\nThere's already a mark there! Try again.")


while is_running == True:   
    player_one()
    player_two()
