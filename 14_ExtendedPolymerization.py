from aoc import get_input

from collections import defaultdict


def parse_input(data):
    data = data.split("\n")

    polymer = data[0]
    instructions = {}
    pairs = defaultdict(int)

    for line in data[2:]:
        instructions[line[0:2]] = line[-1]

    for idx in range(0, len(polymer) - 1):
        a = polymer[idx]
        b = polymer[idx+1]
        pairs[a+b] += 1

    return pairs, instructions


def polymerize(pairs, instructions, iterations=1):

    if iterations == 0:
        return pairs

    result = defaultdict(int)
    for pair, count in pairs.items():
        result[pair[0] + instructions[pair]] += count
        result[instructions[pair] + pair[1]] += count

    return polymerize(result, instructions, iterations - 1)


def score(pairs):

    totals = defaultdict(int)
    for pair, count in pairs.items():
        totals[pair[0]] += count

    totals[data.split("\n")[0][-1]] += 1

    mx = max([count for item, count in totals.items()])
    mn = min([count for item, count in totals.items()])

    return mx - mn


if __name__ == "__main__":
    data = get_input(14, small=False)

    pairs, instructions = parse_input(data)

    print("Part 1:")
    print(score(polymerize(pairs, instructions, 10)))

    print("Part 2:")
    print(score(polymerize(pairs, instructions, 40)))

    print("Part find your maximum recursion depth:")
    print(score(polymerize(pairs, instructions, 980)))
