from aoc import get_input

# Needed for visualizations
import time
import colorama
colorama.init()


FLASH_ENERGY_LEVEL = 10
GRID_SIZE = 10
PRETTY_PRINT_SPEED = 0.1


# Returns all adjacent coordinates for x and y
def get_adjacents(x, y):
    adjacents = []

    for x2 in range(max(0, x-1), min(GRID_SIZE - 1, x+1) + 1):
        for y2 in range(max(0, y-1), min(GRID_SIZE - 1, y+1) + 1):
            if not (x2 == x and y2 == y):
                adjacents.append((x2, y2))

    return adjacents


# Runs one cycle
def cycle(data, pretty=False):
    flashes = set([])
    for y, line in enumerate(data):
        for x, _ in enumerate(line):
            data[y][x] += 1
            if data[y][x] == FLASH_ENERGY_LEVEL:
                flashes.add((x, y))

    for coordinate in flashes:
        flash(*coordinate)

    score = 0
    for y, line in enumerate(data):
        for x, _ in enumerate(line):
            if data[y][x] >= FLASH_ENERGY_LEVEL:
                data[y][x] = 0
                score += 1

    # Visualization
    if pretty:
        pretty_print(data)

    return score


# "Flashes" at the given coordinate
def flash(x, y):
    coordinates = get_adjacents(x, y)
    flashes = set([])

    for coordinate in coordinates:
        x, y = coordinate
        data[y][x] += 1
        if data[y][x] == FLASH_ENERGY_LEVEL:
            flashes.add((x, y))

    for coordinate in flashes:
        flash(*coordinate)


# Visualization
def pretty_print(data):

    time.sleep(PRETTY_PRINT_SPEED)

    for row in data:
        line = ""
        for n in row:
            if n == 0:
                line += colorama.Back.RED + str(n) + colorama.Style.RESET_ALL
            elif n >= 5:
                line += colorama.Fore.RED + str(n) + colorama.Style.RESET_ALL
            else:
                line += " "

        print("\t" + line)

    print("\033[%d;%dH" % (GRID_SIZE + 5, GRID_SIZE + 5))


# Part 1
def solve(data, cycles):
    return sum([cycle(data) for _ in range(0, cycles)])


# Part 2
def solve2(data):
    loop = 1
    score = cycle(data)
    while score < 100:
        score = cycle(data)
        loop += 1

    return loop


# Don't solve anything, just run the visualization forever
def be_pretty(data):
    while True:
        cycle(data, True)


def get_data():
    return [[int(c) for c in line] for line in get_input(11).split("\n")]


if __name__ == "__main__":

    print("Part 1:")
    data = get_data()
    print(solve(data, 100))
    print("Part 2:")
    data = get_data()
    print(solve2(data))
