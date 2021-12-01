from aoc import get_input


# Part 1
def sonar_sweep(data):
    data = data.split("\n")
    data = list(map(int, data))

    last = data[0]
    count = 0
    for depth in data[1:]:
        if depth > last:
            count += 1
            
        last = depth
    
    return count

# Part 2
def sliding_sonar_sweep(data):
    data = data.split("\n")
    data = list(map(int, data))

    last = data[0] + data[1] + data[2]
    count = 0
    for index, depth in enumerate(data[1:-2], start=1):
        depth += data[index + 1] + data[index + 2]

        if depth > last:
            count += 1
            
        last = depth
    
    return count


if __name__ == "__main__":
    data = get_input(1)
    print("--------------")
    print("Solution to part 1:")
    print(sonar_sweep(data))
    print("--------------")
    print("Solution to part 2:")
    print(sliding_sonar_sweep(data))
    print("--------------")