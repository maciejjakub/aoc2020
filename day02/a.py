#!/usr/bin/python3

def load_input(path):
    with open(path, "r") as file:
        data = map(str.strip, file.readlines())
    return data

def puzzle(data):
    puzzle_a_count = 0
    puzzle_b_count = 0
    for i in data:
        count, char, password = i.split()
        count_min, count_max = [int(x) for x in count.split("-")]
        char = char.strip(":")
        if count_min <= password.count(char) <= count_max:
            puzzle_a_count += 1
        if (password[count_min - 1] == char) ^ (password[count_max - 1] == char):
            puzzle_b_count += 1
    return (puzzle_a_count, puzzle_b_count)

if __name__ == '__main__':
    data = load_input('./input')
    output = puzzle(data)
    print(f"Puzzle A: {output[0]}")
    print(f"Puzzle B: {output[1]}")
