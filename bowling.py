#  if u are unfamiliar with bowling rules, go check wiki
Spare = '/'
strike = "x"
Invalid = '-'
STRIKESCORE = 10


def score(game):
    result, frame = 0, 1
    in_first_half = True
    max_gamenum = 10
    for roll in range(len(game)):
        if game[roll] == Spare:
            result += STRIKESCORE - last
        else:
            result += get_value(game[roll])
        if frame < max_gamenum and get_value(game[roll]) == STRIKESCORE:
            if game[roll] == Spare:
                result += get_value(game[roll+1])
            elif game[roll].lower() == strike:
                result += get_value(game[roll+1])
                frame += 1
                if game[roll+2] == Spare:
                    result += STRIKESCORE - get_value(game[roll+1])
                else:
                    result += get_value(game[roll+2])
        last = get_value(game[roll])
        if not in_first_half:
            frame += 1
        if in_first_half is True:
            in_first_half = False
        else:
            in_first_half = True
        if game[roll].lower() == strike:
            in_first_half = True
    return result


def get_value(char):
    try:
        return int(char)
    except ValueError:
        if char.lower() == strike or char == Spare:
            return STRIKESCORE
        elif char == Invalid:
            return 0
        raise ValueError()
