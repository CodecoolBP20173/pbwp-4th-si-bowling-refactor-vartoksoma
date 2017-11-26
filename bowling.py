Spare = '/'
Strike = "X"
strike = "x"
Invalid = '-'
STRIKESCORE = 10


def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for turn in range(len(game)):
        if game[turn] == Spare:
            result += STRIKESCORE - last
        else:
            result += get_value(game[turn])
        if frame < STRIKESCORE and get_value(game[turn]) == STRIKESCORE:
            if game[turn] == Spare:
                result += get_value(game[turn+1])
            elif game[turn] == Strike or game[turn] == strike:
                result += get_value(game[turn+1])
                if game[turn+2] == Spare:
                    result += STRIKESCORE - get_value(game[turn+1])
                else:
                    result += get_value(game[turn+2])
        last = get_value(game[turn])
        if not in_first_half:
            frame += 1
        if in_first_half is True:
            in_first_half = False
        else:
            in_first_half = True
        if game[turn] == Strike or game[turn] == strike:
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char == Strike or char == strike:
        return STRIKESCORE
    elif char == Spare:
        return STRIKESCORE
    elif char == Invalid:
        return 0
    else:
        raise ValueError()
