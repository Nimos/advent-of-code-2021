from aoc import get_input

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1

        self.x2 = x2
        self.y2 = y2


def parse_input(data):
    data = data.split("\n")

    lines = []

    max_x = 0
    max_y = 0

    for line in data:
        line = line.split(" ")
        p1 = tuple(map(int, line[0].split(",")))
        p2 = tuple(map(int, line[2].split(",")))

        if p1[0] > max_x:
            max_x = p1[0]
        if p2[0] > max_x:
            max_x = p2[0]
        if p1[1] > max_y:
            max_y = p1[1]
        if p2[1] > max_y:
            max_y = p2[1]

        lines.append(Line(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])))
    
    grid = []

    for _ in range(0, max_y +1):
        grid.append([0] * (max_x + 1))

    return grid, lines
    

def draw_lines(grid, lines, include_diagonals = True):
    for line in lines:
        # Vertical
        if line.x1 == line.x2:
            if line.y1 > line.y2:
                iterator = range(line.y2, line.y1 + 1)
            else:
                iterator = range(line.y1, line.y2 + 1)

            for y in iterator:
                grid[y][line.x1] += 1
        # Horizontal
        elif line.y1 == line.y2:
            if line.x1 > line.x2:
                iterator = range(line.x2, line.x1 + 1)
            else:
                iterator = range(line.x1, line.x2 + 1)

            for x in iterator:
                grid[line.y1][x] += 1
        # Diagnoal
        elif include_diagonals:
            x_direction = 1 if line.x1 < line.x2 else -1
            x = line.x1

            y_direction = 1 if line.y1 < line.y2 else -1
            y = line.y1

            for _ in range(0, abs(line.y1 - line.y2) + 1):
                grid[y][x] += 1
                x += x_direction 
                y += y_direction


    return grid

def print_grid(grid):
    for line in grid:
        print(line)

def get_solution(grid):
    solution = 0
    for line in grid:
        for num in line:
            if num >= 2:
                solution += 1

    return solution

if __name__ == "__main__":
    data = get_input(5)


    print("Part 1:")
    grid, lines = parse_input(data)
    draw_lines(grid, lines, include_diagonals=False)
    print(get_solution(grid))

    print("Part 2:")
    grid, lines = parse_input(data)
    draw_lines(grid, lines)
    print(get_solution(grid))

    
