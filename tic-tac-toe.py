board = [['-'for i in range(3)]for j in range(3)]

def start_game():
    print('Welcome to tic-tac-toe!')
    print('Player_1 - X\nPlayer_2 - 0')
    print('x - row`s number')
    print('y - column`s number')

def board_view():
    print('-------------')
    print('    0 | 1 | 2')
    for i, j in enumerate(board):
        print(f"{i} | {' | '.join(j)}")
    print('-------------')

def player_moves(arg):
    print("Player_1 moves" if arg == "X" else "Player_2 moves")

def input_data(arg):
    while True:
        player_answer = input(f"Enter numbers of xy(merged):")
        if player_answer and len(player_answer) == 2:
            if all([player_answer[0] in '012',
                    player_answer[1] in '012',
                    player_answer[0].isdigit(), player_answer[1].isdigit()]):
                a, b = int(player_answer[0]), int(player_answer[1])
                if board[a][b] not in 'X0':
                    board[a][b] = arg
                    break
                else:
                    print('This cell is already taken!')
                    continue
            else:
                print('Invalid input!')
                continue
        else:
            print('Invalid input!')
            continue

def check_win(arg):
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for each in win_coord:
        if all([arg[each[0][0]][each[0][1]] not in '-',
                arg[each[1][0]][each[1][1]] not in '-',
                arg[each[2][0]][each[2][1]] not in '-']):
            if arg[each[0][0]][each[0][1]] == arg[each[1][0]][each[1][1]] == arg[each[2][0]][each[2][1]]:
                return True
    return False

def main():
    counter = 0
    while True:
        board_view()
        if counter % 2 == 0:
            player_moves('X')
            input_data('X')
        else:
            player_moves('O')
            input_data('O')
        counter += 1
        if counter > 4:
            if check_win(board):
                print('Player_1 wins!' if counter % 2 != 0 else 'Player_2 wins!')
                board_view()
                break
        if counter == 9:
            print('Dead heat!')
            break

start_game()
main()