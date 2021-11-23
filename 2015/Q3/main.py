
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
    position = [0, 0]
    gifted = {'[0, 0]': 1}

    with open('directions.txt') as fp:
        instructions = fp.readlines()[0]
        for direction in instructions:
            key = direction_to_numeric(direction, position)
            position = key      # new position

            key = str(key)
            if key in gifted.keys():
                gifted[key] += 1
            else:
                gifted.update({key: 1})

    print("Ans Q3a::   Santa visited {} homes atleast once".format(len(gifted)))
