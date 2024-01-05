import math

SCORE_LIMITS = {"red": 12, "green": 13, "blue": 14}


# Read the data file
def read_data(path: str) -> str:
    with open(path, "r") as file:
        return file.read()


# Separate the game ID indicator from its core content
def split_game(game: str) -> [str, str]:
    return [section.strip() for section in game.split(":")]


# Test whether the given score fits within the given limits
# todo: Streamline
def validate_score(score, limits):
    for colour in limits.keys():
        if score[colour] > limits[colour]:
            return False
    return True


# Interprets the result of the given game. Returns its ID and whether it's legal
def interpret_game(game: str) -> [str, bool]:
    sections = split_game(game)
    game_ID = int(sections[0].split()[1])
    core = sections[1]

    max_score = {"red": 0, "green": 0, "blue": 0}
    for round in core.split(";"):
        for amount, colour in (turn.split() for turn in round.split(",")):
            max_score[colour] = max(max_score[colour], int(amount))

    return game_ID, math.prod(max_score.values())


def interpret_data(data: str):
    total = 0
    for game in data.splitlines():
        _, power = interpret_game(game)
        total += power
    return total


if __name__ == '__main__':
    data = read_data("data.txt")
    print(interpret_data(data))
