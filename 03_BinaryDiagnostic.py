from aoc import get_input


def get_diagnostic(data):

    # Initialize counter list with number length
    counters = [0] * len(data[0])

    for num in data:
        for idx, bit in enumerate(num):
            counters[idx] += int(bit)
    
    half = len(data) / 2

    gamma = ""
    epsilon = ""
    for count in counters:
        if count >= half:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return gamma, epsilon, int(gamma, 2) * int(epsilon, 2)


MODE_OXYGEN = 0
MODE_CO2 = 1

def get_life_support(data):
    
    # Recursive because why not?
    def filter_life_support(data, mode, index = 0):

        # return condition
        if len(data) == 1:
            return data[0]

        # Run the code from part 1 to get the "key"
        diagnostic = get_diagnostic(data)

        # index for the tuple returned by the part 1 code
        key = diagnostic[mode]

        # filter numbers by key
        filtered = []
        for num in data:
            if num[index] == key[index]:
                filtered.append(num)
        
        # keep going
        return filter_life_support(filtered, mode, index + 1)


    oxygen = filter_life_support(data, MODE_OXYGEN)
    co2 = filter_life_support(data, MODE_CO2)

    return oxygen, co2, int(oxygen, 2) * int(co2, 2)

if __name__ == "__main__":
    data = get_input(3)
    data = data.split("\n")


    print("Part 1:")
    print(get_diagnostic(data))

    print("Part 2:")
    print(get_life_support(data))