from aoc import get_input


def find_low_points(data):
    data = [[int(c) for c in line] for line in data.split("\n")]

    risk_level = 0
    low_points = []

    for y_index, line in enumerate(data):
        for x_index, height in enumerate(line):
            if height < min(get_adjacent_heights(data, x_index, y_index)):
                risk_level += height + 1
                low_points.append((x_index, y_index))

    return risk_level, low_points


def get_adjacent_heights(data, x, y):
    return [get_height(data, x, y) for x, y in get_adjacents(x, y)]


def get_adjacents(x, y):
    return (
        (x, y-1),
        (x-1, y),
        (x+1, y),
        (x, y+1)
    )


def get_basins(data):
    _, low_points = find_low_points(data)

    data = [[int(c) for c in line] for line in data.split("\n")]

    basins = []
    for start in low_points:
        basin = fill_basin([start], data)
        basins.append(basin)

    return basins


def fill_basin(basin, data, fill_height=None):
    # Initial height is the height of the low point
    if not fill_height:
        fill_height = data[basin[0][1]][basin[0][0]]

    # 9 spots are never part of a basin so we can stop here
    if fill_height >= 9:
        return basin

    for coordinate in basin:
        x, y = coordinate

        for x2, y2 in get_adjacents(x, y):
            height = get_height(data, x2, y2)
            if height > fill_height and height < 9 and (x2, y2) not in basin:
                basin.append((x2, y2))

    return fill_basin(basin, data, fill_height+1)


def get_basin_score(basins):
    result = 1

    for n in sorted([len(basin) for basin in basins])[-3:]:
        result *= n
    return result


def get_height(data, x, y):
    if (y < 0 or x < 0):
        return float('inf')

    try:
        return data[y][x]
    except IndexError:
        return float('inf')


if __name__ == "__main__":
    data = get_input(9)

    print("Part 1:")
    print(find_low_points(data)[0])

    print("Part 2:")
    print(get_basin_score(get_basins(data)))
