def render_data(datafile):
    bingo_dict = {}
    loop_counter = 0

    try:
        with open(datafile) as fp:
            bingo_numeric = fp.readline().strip('\n').split(',')
            while True:
                line = fp.readline(3)

                if line == '\n':
                    continue

                bingo_matrix = [[0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0]]

                for j in range(5):
                    for i in range(5):
                        line = line.strip(" ")
                        bingo_matrix[j][i] = int(line)
                        line = fp.readline(3)

                loop_counter += 1
                tmp = bingo_matrix
                bingo_dict.update({str(loop_counter): tmp})

                if loop_counter == 100:
                    break

    except FileNotFoundError:
        raise FileNotFoundError('Cannot find specified file!')

    finally:
        return bingo_numeric, bingo_dict


def check_for_bingo(number, games):
    for key, game in games.items():
        coordinates = []
        for bingo_selector in range(5):
            bingo_row_checker = {0: 0,
                                 1: 0,
                                 2: 0,
                                 3: 0,
                                 4: 0}
            bingo_col_checker = {0: 0,
                                 1: 0,
                                 2: 0,
                                 3: 0,
                                 4: 0}
            try:
                index = game[bingo_selector].index(number)
                game[bingo_selector][index] = str(game[bingo_selector][index])+'x'
            except ValueError:
                continue

            coordinates.append([index, bingo_selector])

            for i in range(5):
                for j in range(5):
                    if type(game[i][j]) != int and 'x' in game[i][j]:
                        coordinates.append([i, j])
                        bingo_row_checker[i] += 1
                        bingo_col_checker[j] += 1

            ret = False
            for val in bingo_row_checker.values():
                if val == 5:
                    ret = True

            for val in bingo_col_checker.values():
                if val == 5:
                    ret = True

            if ret:
                return game


def check_for_last_bingo(number, games, bingo_boards):
    for key, game in games.items():
        if key in bingo_boards.keys():
            continue

        coordinates = []
        for bingo_selector in range(5):
            bingo_row_checker = {0: 0,
                                 1: 0,
                                 2: 0,
                                 3: 0,
                                 4: 0}
            bingo_col_checker = {0: 0,
                                 1: 0,
                                 2: 0,
                                 3: 0,
                                 4: 0}
            try:
                index = game[bingo_selector].index(number)
                game[bingo_selector][index] = str(game[bingo_selector][index])+'x'
            except ValueError:
                continue

            coordinates.append([index, bingo_selector])

            for i in range(5):
                for j in range(5):
                    if type(game[i][j]) != int and 'x' in game[i][j]:
                        coordinates.append([i, j])
                        bingo_row_checker[i] += 1
                        bingo_col_checker[j] += 1

            bingo = False
            for val in bingo_row_checker.values():
                if val == 5:
                    bingo = True

            for val in bingo_col_checker.values():
                if val == 5:
                    bingo = True

            if bingo:
                bingo_boards.update({key: number})

    return bingo_boards


def question_4a(number, games):
    bingo = False
    index = 0
    while not bingo:
        call = int(number[index])
        game = check_for_bingo(call, games)
        index += 1
        if game is not None:
            break

    sum = 0
    for i in range(5):
        for j in range(5):
            if type(game[i][j]) == int:
                sum += game[i][j]

    answer = sum * int(calling_number[index-1])
    print('Ans Q4a:: Sum of unmarked numbers times the calling number: {}'.format(answer))


def question_4b(number, games):
    list_of_bingo_boards = {}  # {board: calling_number}
    index = 0
    for i in range(len(number)):
        call = int(number[index])
        tmp = check_for_last_bingo(call, games, list_of_bingo_boards)

        if tmp is not None:
            list_of_bingo_boards = tmp
        index += 1

    winning_board = list(list_of_bingo_boards.keys())[len(list_of_bingo_boards)-1]
    winning_number = list_of_bingo_boards[winning_board]
    game = games[winning_board]
    sum = 0
    for i in range(5):
        for j in range(5):
            if type(game[i][j]) == int:
                sum += game[i][j]

    answer = sum * int(winning_number)
    print('Ans Q4b:: Sum of unmarked numbers times the calling number of last bingo board: {}'.format(answer))


if __name__ == '__main__':
    filename = "../instructions/bingo"
    calling_number, bingo_games = render_data(filename)

    question_4a(calling_number, bingo_games)
    question_4b(calling_number, bingo_games)



