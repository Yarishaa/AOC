
def direction_to_numeric(symbol, pos):
    x = pos[0]
    y = pos[1]

    if symbol == '>':
        x = x + 1
    elif symbol == '<':
        x = x - 1
    elif symbol == '^':
        y = y + 1
    elif symbol == 'v':
        y = y - 1
    else:
        raise ValueError('Unrecognized symbol: {}'.format(symbol))

    return [x, y]


if __name__ == '__main__':
    santa_position = [0, 0]
    santa_combined = [0, 0]
    robo_position = [0, 0]
    gifted = {'santa': {'[0, 0]': 1}, 'combined': {'[0, 0]': 2}}

    with open('directions.txt') as fp:
        instructions = fp.readlines()[0]

    for idx in range(len(instructions)):
        pos1 = direction_to_numeric(instructions[idx], santa_position)
        santa_position = pos1
        pos1 = str(pos1)
        if pos1 in gifted['santa'].keys():
            gifted['santa'][pos1] += 1
        else:
            gifted['santa'].update({pos1: 1})

        if not idx % 2:
            pos1 = direction_to_numeric(instructions[idx], santa_combined)
            santa_combined = pos1
            pos1 = str(pos1)

            pos2 = direction_to_numeric(instructions[idx+1], robo_position)
            robo_position = pos2
            pos2 = str(pos2)

            if pos1 == pos2:
                if pos1 in gifted['combined'].keys():
                    gifted['combined'][pos1] += 1
                else:
                    gifted['combined'].update({pos1: 2})
            else:
                if pos1 in gifted['combined'].keys():
                    gifted['combined'][pos1] += 1
                else:
                    gifted['combined'].update({pos1: 1})

                if pos2 in gifted['combined'].keys():
                    gifted['combined'][pos2] += 1
                else:
                    gifted['combined'].update({pos2: 1})

    print("Ans Q3a::   Santa visited {} homes atleast once".format(len(gifted['santa'])))
    print("Ans Q3b::   Santa and Robo visited {} homes atleast once".format(len(gifted['combined'])))
