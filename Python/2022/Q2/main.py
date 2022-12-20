"""
A : Rock     : X   val 1
B : Paper    : Y   val 2
C : Scissors : Z   val 3

Score:
Loss : 0 pts
Draw : 3 pts
Win  : 6 pts
"""
moves = {
    'A' : ['ROCK', 1],
    'B' : ['PAPER', 2],
    'C' : ['SCISSOR', 3],
    'X' : ['ROCK', 1],
    'Y' : ['PAPER', 2],
    'Z' : ['SCISSOR', 3]
}
result_scores = {
    'WIN' : 6,
    'DRAW' : 3,
    'LOSS' : 0
}
prediction = {
    'X' : 'LOSS',
    'Y' : 'DRAW',
    'Z' : 'WIN'
}

def _predict_result(res):
    opponent, result = res.split(' ')
    match_point = 0

    if opponent == 'A':     # ROCK
        if result == 'X':
            match_point = result_scores[prediction['X']] + moves['Z'][1]
        elif result == 'Y':
            match_point = result_scores[prediction['Y']] + moves['X'][1]
        elif result == 'Z':
            match_point = result_scores[prediction['Z']] + moves['Y'][1]
    elif opponent == 'B':   # PAPER
        if result == 'X':
            match_point = result_scores[prediction['X']] + moves['X'][1]
        elif result == 'Y':
            match_point = result_scores[prediction['Y']] + moves['Y'][1]
        elif result == 'Z':
            match_point = result_scores[prediction['Z']] + moves['Z'][1]
    elif opponent == 'C':  # SCISSOR
        if result == 'X':
            match_point = result_scores[prediction['X']] + moves['Y'][1]
        elif result == 'Y':
            match_point = result_scores[prediction['Y']] + moves['Z'][1]
        elif result == 'Z':
            match_point = result_scores[prediction['Z']] + moves['X'][1]

    return match_point


def _game_result(res):
    opponent, self = res.split(' ')
    match_point = 0

    if opponent == 'A':
        if self == 'Y':
            match_point = result_scores['WIN'] + moves['Y'][1]
        elif self == 'Z':
            match_point = result_scores['LOSS'] + moves['Z'][1]
        elif self == 'X':
            match_point = result_scores['DRAW'] + moves['X'][1]
    elif opponent == 'B':
        if self == 'Y':
            match_point = result_scores['DRAW'] + moves['Y'][1]
        elif self == 'Z':
            match_point = result_scores['WIN'] + moves['Z'][1]
        elif self == 'X':
            match_point = result_scores['LOSS'] + moves['X'][1]
    elif opponent == 'C':
        if self == 'Y':
            match_point = result_scores['LOSS'] + moves['Y'][1]
        elif self == 'Z':
            match_point = result_scores['DRAW'] + moves['Z'][1]
        elif self == 'X':
            match_point = result_scores['WIN'] + moves['X'][1]

    return match_point


def question_2a(strat_lst):
    total_score = 0
    for match in strat_lst:
        total_score += _game_result(match)

    print('Total score if played exactly like sheetcheat is {} pts'.format(total_score))


def question_2b(strat_lst):
    total_score = 0
    for match in strat_lst:
        total_score += _predict_result(match)

    print('Total score if played exactly like sheetcheat is {} pts'.format(total_score))


if __name__ == '__main__':
    strategy = []
    try:
        with open('../instructions/rps_strategy.csv') as fp:
            for game in fp.readlines():
                strategy.append(game.strip('\n'))

    except FileNotFoundError as e:
        print(e)

    question_2a(strategy)
    question_2b(strategy)

