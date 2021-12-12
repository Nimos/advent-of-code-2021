from aoc import get_input

START_ROOM = "start"
END_ROOM = "end"


# Parse the input into a list of dicts that have all the connections
def parse_tree(data):
    data = data.split("\n")
    caves = {}

    for edge in data:
        edge = edge.split("-")
        if not caves.get(edge[0]):
            caves[edge[0]] = []
        if not caves.get(edge[1]):
            caves[edge[1]] = []

        caves[edge[0]].append(edge[1])
        caves[edge[1]].append(edge[0])

    return caves


def walk_caves(caves, path=[START_ROOM], max_visits=1):
    cur = path[-1]

    if cur == END_ROOM:
        return [path]

    # Part 2: After visiting a single small cave once,
    # no other small caves may be visited twice
    if max_visits > 1 and path.count(cur) == max_visits and cur.islower():
        max_visits = 1

    # A wise soul once said:
    # "if you do it in python you gotta do list comprehensions"
    paths = [
        walk_caves(caves, path + [cave], max_visits)
        for cave in caves[cur]
        if cave != START_ROOM and path.count(cave) < max_visits or cave.isupper()
    ]

    # Flatten the returned list of lists
    flat = []
    for branches in paths:
        for path in branches:
            flat.append(path)

    return flat


if __name__ == "__main__":

    data = get_input(12, small=False)
    caves = parse_tree(data)

    print("Part 1:")
    paths = walk_caves(caves)
    print(len(paths))

    print("Part 2:")
    paths = walk_caves(caves, max_visits=2)
    print(len(paths))
