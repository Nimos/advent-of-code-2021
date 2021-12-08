###
#
# Please look away I don't like this one but I don't have time to refactor it either :()
#

from aoc import get_input
import string

SEGMENTS = 7

SIGNALS = [
    [1, 1, 1, 0, 1, 1, 1], # 0
    [0, 0, 1, 0, 0, 1, 0], # 1
    [1, 0, 1, 1 ,1, 0, 1], # 2
    [1, 0, 1, 1, 1, 0, 1], # 3
    [0, 1, 1, 1, 0, 1, 0], # 4
    [1, 1, 0, 1, 0, 1, 1], # 5
    [1, 1, 0, 1, 1, 1, 1], # 6
    [1, 0, 1, 0, 0, 1, 0], # 7
    [1, 1, 1, 1, 1, 1, 1], # 8
    [1, 1, 1, 1, 0, 1, 1], # 9
]

COUNTS = [sum([s for s in l if s]) for l in SIGNALS]

COUNTS_MAPPING = [[] for _ in range(0, SEGMENTS + 1)]

LETTERS_MAPPING = {letter:index for index,letter in enumerate(string.ascii_lowercase[:SEGMENTS])}


for number, count in enumerate(COUNTS):
    COUNTS_MAPPING[count].append(number)

def get_sequence(data):
    sequence = data.replace(" | ", " ").split(" ")
    sequence = replace_letters(sequence)
    return sequence

def replace_letters(sequence):

    sequence = [set([LETTERS_MAPPING[letter] for letter in word]) for word in sequence]
    return sequence
    


def search(data):
    sequence = get_sequence(data)

    possible_numbers = [set(COUNTS_MAPPING[len(signal)]) for signal in sequence]
    number_signals = [set([]) for _ in range(0, 10)]

    solved = False
    while not solved:
        for index, p in enumerate(possible_numbers):
            if len(p) == 1:
                number_signals[next(iter(p))] = sequence[index]


        for index, signal in enumerate(sequence):
            for number_signal in number_signals:
                if not number_signal:
                    continue
                
                if (signal.issuperset(number_signals[1])):
                    possible_numbers[index] -= set([2, 5, 6])
                else:
                    possible_numbers[index] -= set([0, 1, 3, 4, 7, 8, 9])

                if not number_signals[7]:
                    continue
                if (signal.issuperset(number_signals[7])):
                    possible_numbers[index] -= set([2, 4, 5, 6])
                else:
                    possible_numbers[index] -= set([0, 3, 7, 8, 9])

                if not number_signals[3]:
                    continue
                if (signal.issuperset(number_signals[3])):
                    possible_numbers[index] -= set([0, 1, 2, 4, 5, 6, 7])
                else:
                    possible_numbers[index] -= set([3, 8, 9])

                if not number_signals[6] or not number_signals[1]:
                    continue
                if signal.issuperset(number_signals[1] - number_signals[6]):
                    possible_numbers[index] -= set([5, 6])
                else:
                    possible_numbers[index] -= set([0,1,2,3,4,7,8,9])
        
        solved = len(possible_numbers) == len([n for n in possible_numbers if len(n) == 1])
        
    return int("".join([str(s.pop()) for s in possible_numbers[-4:]]))
            



if __name__ == "__main__":
    data = get_input(8)

    r = 0
    for d in data.split("\n"):
        r += search(d)


    print(r)
    

    