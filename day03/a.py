#!/usr/bin/python3

def load_input(path):
    with open(path, "r") as file:
        data = [x.strip() for x in file.readlines()]
    return data

def puzzle(right, down):
    x, y = (0, 0)
    count = 0
    for i in data:
        x += right
        y += down
        if x >= len(i):
            x -= len(i)
        if y >= len(data):
            return count
        if data[y][x] == "#":
            count += 1

if __name__ == '__main__':
    data = load_input("./input")
    print(f"Puzzle A: {puzzle(3, 1)}")
    
    puzzle_b_product = puzzle(1, 1) * \
                       puzzle(3, 1) * \
                       puzzle(5, 1) * \
                       puzzle(7, 1) * \
                       puzzle(1, 2)
    print(f"Puzzle B: {puzzle_b_product}")
