game_board = list(range(1, 10))
wins_comb = (
    (1, 2, 3), (4, 5, 6), (7, 8, 9),
    (1, 4, 7), (2, 5, 8), (3, 6, 9),
    (1, 5, 9), (3, 5, 7)
)


def draw_board():
    print('-------------')
    for i in range(3):
        print('|', game_board[0 + i * 3], '|', game_board[1 + i * 3], '|', game_board[2 + i * 3], '|')
    print('-------------')


def player_step(token):
    while True:
        value = input('Куда поставить: ' + token + '? ')
        if not (value in '123456789'):
            print('Ошибка. Повторите ввод')
            continue
        value = int(value)
        if not (0 < value < 10):
            print('Неверное значени. Повторите!')
            continue
        if str(game_board[value - 1]) in 'XO':
            print('Клетка занята.')
            continue
        game_board[value - 1] = token
        break


def check_win():
    for i in wins_comb:
        if game_board[i[0] - 1] == game_board[i[1] - 1] == game_board[i[2] - 1]:
            return game_board[i[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            player_step('X')
        else:
            player_step('O')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(winner, 'выиграл!')
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('Ничья!')
            break


main()
