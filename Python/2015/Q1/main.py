floor = 0
with open('Q1/instruction.txt') as fp:
    basement = True
    characters = fp.readline()
    for i in range(len(characters)):
        if characters[i] == '(':
            floor += 1
        elif characters[i] == ')':
            floor -= 1
        else:
            print('unknown character {}'.format(characters[i]))

        if floor == -1 and basement:
            basement = False
            first_time_entering_basement = i + 1    # Account for zeroindex



print("Ans Q1a::   Santa is on floor: {}".format(floor))
print("Ans Q1b::   Santa enters the basement at index: {}".format(first_time_entering_basement))
