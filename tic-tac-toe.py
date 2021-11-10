board = [['-'for i in range(3)]for j in range(3)]

def start_game():
    print('Welcome to tic-tac-toe!')
    print('Player1 - X\nPlayer2 - 0')
    print('x - row`s number')
    print('y - column`s number')

def board_view():
    print('-------------')
    print('    0 | 1 | 2')
    for i, j in enumerate(board):
        print(f"{i} | {' | '.join(j)}")
    print('-------------')

def player_moves(arg):
    print("Player1 moves" if arg == "X" else "Player2 moves")

def input_data(arg):
    while True:
        player_answer = input(f"Enter xy:")
        if player_answer:
            a, b = int(player_answer[0]), int(player_answer[1])
            if all([(len(player_answer)) == 2,
                    (0 > a > 2 or 0 > a > 2)]):
                if board[a][b] not in 'X0':
                    board[a][b] = arg
                    break
                else:
                    print('Эта клеточка уже занята')
                    continue
            else:
                print('Некорректный ввод!')
                continue
        else:
            print('Некорректный ввод!')
            continue

def check_win(arg):
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for each in win_coord:
        if all([arg[each[0][0]][each[0][1]] not in '-',
                arg[each[1][0]][each[1][1]] not in '-',
                arg[each[2][0]][each[2][1]] not in '-']):
            if (arg[each[0][0]][each[0][1]] == arg[each[1][0]][each[1][1]] == arg[each[2][0]][each[2][1]]):
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
                print('Выиграл Player1!' if counter % 2 != 0 else 'Выиграл Player2!')
                board_view()
                break
        if counter == 9:
            print('Ничья!')
            break

start_game()
main()