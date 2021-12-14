from aoc import get_input


def read_data(data):
    data = data.split("\n")

    points = set()
    instructions = []
    for line in data:
        if line == "":
            continue

        if line[0] == "f":
            line = line.split(" ")[-1].split("=")
            instructions.append((line[0], int(line[1])))
        else:
            line = line.split(",")
            points.add((int(line[0]), int(line[1])))

    return points, instructions


def fold(points, coordinate):
    axis = 0 if coordinate[0] == "x" else 1
    pos = coordinate[1]

    updated = set([])
    for point in points:
        if point[axis] > pos:
            point = list(point)
            point[axis] = pos - (point[axis] - pos)
        
        updated.add(tuple(point))

    
    return updated


def print_paper(points):
    max_x = max([p[0] for p in points])
    max_y = max([p[1] for p in points])

    grid = [
        ["." for _ in range(0, max_x + 1)]
        for _ in range(0, max_y + 1)
    ]

    for p in points:
        grid[p[1]][p[0]] = "#"

    for line in grid:
        print("".join(line))

if __name__ == "__main__":

    data = get_input(13, small=False)

    points, instructions = read_data(data)
    print("Part 1:")
    points = fold(points, instructions[0])
    print(len(points))

    for i in instructions[1:]:
        points = fold(points, i)
    
    print_paper(points)
