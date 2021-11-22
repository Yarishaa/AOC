
floor = 0
with open('instruction.txt') as fp:
    for char in fp.readline():
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        else:
            print('unknown character {}'.format(char))

print("Santa is on floor: {}".format(floor))
