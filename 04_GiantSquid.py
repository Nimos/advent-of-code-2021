from aoc import get_input

# Could parse this dynamically from the 
# input but I've never seen a 6x6 bingo
BOARD_SIZE = 5

# Parses the input file into boards and a sequence
def parse_input(data):
    data = data.split("\n")

    sequence = list(map(int, data[0].split(",")))
    
    boards = [[]]
    board_index = 0

    # We'll just flatten the boards into a list of lists
    for line in data[2:]:
        # empty line -> next board
        if line == "":
            board_index += 1
            boards.append([])
            continue
        
        line = [int(n) for n in line.split(" ") if n != ""]

        boards[board_index].extend(line)
    
    return sequence, boards

# Checks if the board wins with the given sequence
# We're going for a stateless solution, so instead of
# marking off squares we'll just check them against the
# sequence
def check_board(board, sequence):
    # Check rows
    for row_start in range(0, BOARD_SIZE * BOARD_SIZE, BOARD_SIZE):
        marked_numbers = [n for n in board[row_start:row_start + BOARD_SIZE] if n in sequence]
        if len(marked_numbers) == BOARD_SIZE:
            return True

    # Check columns
    for column_start in range(0, BOARD_SIZE - 1):
        column = [board[index] for index in range(column_start, column_start + BOARD_SIZE * BOARD_SIZE, BOARD_SIZE)]
        marked_numbers = [n for n in column if n in sequence]
        if len(marked_numbers) == BOARD_SIZE:
            return True
        
    return False


# Score = sum of all unmarked numbers multiplied by the
# winning number
def calculate_score(board, sequence):
    unmarked_numbers = [n for n in board if n not in sequence]

    score = 0
    for n in unmarked_numbers:
        score += n

    score *= sequence[-1]

    return score 


# Part 1
def game(data):
    sequence, boards = parse_input(data)

    # Go through the numbers in the sequence sequetially (as we do with sequences)
    # Find the first board that wins and return the score
    for step in range(BOARD_SIZE - 1, len(sequence)):
        for board in boards:
            if check_board(board, sequence[0:step]):
                return calculate_score(board, sequence[0:step])


# Part 2
def game2(data):
    sequence, boards = parse_input(data)

    wins = []
    last_win = 0

    # Go through the sequence and mark off boards that have won 
    # and the position in the sequence that the last win occured
    for step in range(BOARD_SIZE - 1, len(sequence)):
        for board_index, board in enumerate(boards):
            if board_index not in wins:
                if check_board(board, sequence[0:step]):
                    wins.append(board_index)
                    last_win = step
    
    # When we're done we have the final winning board and we can
    # calculate the score as usual
    final_index = wins[-1]

    return calculate_score(boards[final_index], sequence[0:last_win])


if __name__ == "__main__":
    data = get_input(4)


    print("Part 1:")
    print(game(data))

    print("Part 2:")
    print(game2(data))