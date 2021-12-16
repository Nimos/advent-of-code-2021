from aoc import get_input
from datetime import datetime

import math

MULTIPLIER = 5

def get_adjacents(graph, x, y):
    adjacents = []

    max_x = len(graph[0]) - 1
    max_y = len(graph) - 1

    if x > 0:
        adjacents.append((x-1, y))
    if x < max_x:
        adjacents.append((x+1, y))
    if y > 0:
        adjacents.append((x, y-1))
    if y < max_y:
        adjacents.append((x, y+1))

    return adjacents


def parse_input(data):
    data = [[[int(n), float('inf')] for n in line] for line in data.split("\n")]
    data[0][0][1] = 0

    return data

def parse_input2(data):
    data = parse_input(data)

    len_x = len(data[0])
    len_y = len(data)

    big_data = [[[0, 0] for _ in range(0, len_x * MULTIPLIER)] for _ in range(0, len_y  * MULTIPLIER)]
    for y in range(0, len_y * MULTIPLIER):
        for x in range(0, len_x * MULTIPLIER):
            num = data[y % len_y][x % len_x][0]
            num = num + math.floor(y/len_y) + math.floor(x/len_x)
            if num >= 10:
                num -= 9
            big_data[y][x] = [num, float('inf')]

    big_data[0][0] = [1, 0]

    return big_data


def find_path(graph):
    start = (0, 0)

    queue = [start]

    while len(queue) > 0:
        x, y = queue.pop(0)
        dist = graph[y][x][1]

        for neighbour in get_adjacents(graph, x, y):
            x, y = neighbour

            if graph[y][x][1] > dist + graph[y][x][0]:
                graph[y][x][1] = dist + graph[y][x][0]
                if (x, y) not in queue:
                    queue.append((x, y))

    print_costs(graph)


def print_costs(graph):
    print("-------------")
    for y in graph:
        print(", ".join([str(x[1]) for x in y]))


if __name__ == "__main__":
    start = datetime.now()
    data = get_input(15, small=False)
    graph = parse_input2(data)
    end = datetime.now()

    start = datetime.now()
    print(find_path(graph))
    end = datetime.now()

    time = end - start

    print("Done in", str(time.microseconds) + "us")
