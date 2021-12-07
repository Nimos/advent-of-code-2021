from aoc import get_input


def get_fuel(data):
    data = list(map(int, data.split(",")))

    median = get_median(data)

    fuel = 0
    for crab in data:
        fuel += abs(crab - median)
    
    return fuel

def get_fuel2(data):
    data = list(map(int, data.split(",")))

    mean = get_mean(data)

    fuel = 0
    for crab in data:
        distance = abs(crab - mean)
        fuel += int((distance * distance + distance)/2)


    return fuel

def get_median(l):
    l = sorted(l)
    length = int(len(l))
    median = sorted(l)[int(length/2)]
    return median

def get_mean(l):
    return int(sum(l)/len(l))

if __name__ == "__main__":
    data = get_input(7)


    print("Part 1:")
    print(get_fuel(data))

    print("Part 2:")
    print(get_fuel2(data))

    