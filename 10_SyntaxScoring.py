from aoc import get_input

MAP = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

SCORES2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


def score_syntax_errors(data):
    data = data.split("\n")

    score1 = 0
    score2 = []
    for line in data:
        stack = []
        corrupted = False
        for char in line:
            if char in "([{<":
                stack.append(char)
            elif char == MAP[stack.pop()]:
                continue
            else:
                corrupted = True
                score1 += SCORES[char]
                break
        if not corrupted and stack:
            line_score = 0
            for char in stack[::-1]:
                line_score *= 5
                line_score += SCORES2[char]
            score2.append(line_score)

    score2 = sorted(score2)[(int((len(score2))/2))]
            
    return score1, score2


if __name__ == "__main__":
    data = get_input(10)

    print("Part 1:")
    print(score_syntax_errors(data))