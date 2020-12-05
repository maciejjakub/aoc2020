#!/usr/bin/python3

def load_input(path):
    with open(path, "r") as file:
        data = [x.strip() for x in file.readlines()]
    return data

def return_seat_id(characters):
    row = puzzle_parser(characters[:7], 0, 128)
    column = puzzle_parser(characters[7:], 0, 8)
    return row * 8 + column

def puzzle_parser(input_string, low, high):
    rng = range(low, high)
    for i in input_string:
        if i == "F" or i == "L":
            high = int(high - len(rng) / 2)
            rng = range(low, high)
        elif i == "B" or i == "R":
            low = int(low + len(rng) / 2)
            rng = range(low, high)
    return rng[0]

def puzzle_a():
    return max(return_seat_id(x) for x in data)

def puzzle_b():
    sorted_ids = sorted(return_seat_id(x) for x in data)
    for i, value in enumerate(sorted_ids):
        if sorted_ids[i + 1] != value + 1: 
            return value + 1

if __name__ == '__main__':
    data = load_input("./input")
    print(f"Puzzle A: {puzzle_a()}")
    print(f"Puzzle B: {puzzle_b()}")
