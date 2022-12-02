# This is already knocked down from a more bloated version I was
# starting to write. Yet it still looks over-engineered...

lines, total_me, total_you = None, 0, 0

# clearly this is not a sustainable encoding beyond
# a couple variable combinations...
OUTCOME_IWIN = ["A Y", "B Z", "C X"]
OUTCOME_ILOSE = ["A Z", "B X", "C Y"]
OUTCOME_IDRAW = ["A X", "B Y", "C Z"]

POINTS_WIN = 6
POINTS_LOSE = 0
POINTS_DRAW = 3

POINTS_ROCK = 1
POINTS_PAPER = 2
POINTS_SCISSORS = 3

ROCK = ['A', 'X']
PAPER = ['B', 'Y']
SCISSORS = ['C', 'Z']


def getChoicePoints(round_line: str) -> tuple:
    you: int = POINTS_ROCK
    me: int = POINTS_ROCK

    your_pick, my_pick = round_line.split()

    if your_pick in PAPER:
        you = POINTS_PAPER
    elif your_pick in SCISSORS:
        you = POINTS_SCISSORS

    if my_pick in PAPER:
        me = POINTS_PAPER
    elif my_pick in SCISSORS:
        me = POINTS_SCISSORS

    return you, me


def processRound(round_line: str) -> None:
    global total_me, total_you

    me, you = 0, 0

    if round_line:
        if round_line in OUTCOME_IWIN:
            me += POINTS_WIN
            you += POINTS_LOSE
        elif round_line in OUTCOME_ILOSE:
            me += POINTS_LOSE
            you += POINTS_WIN
        else:
            me += POINTS_DRAW
            you += POINTS_DRAW

    your_bonus, my_bonus = getChoicePoints(round_line)

    total_you += you + your_bonus
    total_me += me + my_bonus


with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    processRound(line.strip())
