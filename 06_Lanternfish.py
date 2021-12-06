from aoc import get_input

FISH_TIMER = 6
MATURITY_TIMER = 2

def simulate(data, days):
    # This list will the number of fish indexed by their age (or "remaining age")
    ages = [0] * (FISH_TIMER + MATURITY_TIMER + 1)

    # Parse and add the initial fish
    fish = list(map(int, data.split(",")))

    for f in fish:
        ages[f] += 1

    # Simulate the days
    for _ in range(0, days):

        # Progress fish through their age groups and count newly spawned fish
        new_fish = 0
        for age, count in enumerate(ages):
            if age == 0:
                new_fish += count
            else:
                ages[age-1] += count
            
            ages[age] = 0

        # Add newly spawned fish and reset the parents' timers
        ages[FISH_TIMER + MATURITY_TIMER] += new_fish
        ages[FISH_TIMER] += new_fish


    # Finally add up the numbers for the puzzle solution
    total = 0
    for count in ages:
        total += count 

    return total

if __name__ == "__main__":
    data = get_input(6)


    print("Part 1:")
    print(simulate(data, 80))

    print("Part 2:")
    print(simulate(data, 256))

    
