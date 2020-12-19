#!/usr/bin/python3
from collections import Counter

def load_input(path):
    with open(path, "r") as file:
        data = file.read().split("\n\n")
    return data

def puzzle_a(data):
    data = [x.replace("\n", "") for x in data]
    number_of_unique = [len(set(x)) for x in data]
    return sum(number_of_unique)

def puzzle_b(data):
    data = [Counter(x) for x in data]
    data = [sum(value == (x["\n"] + 1) for value in x.values()) for x in data]
    return sum(data)

if __name__ == '__main__':
    data = load_input("./input")
    print(f"Puzzle A: {puzzle_a(data)}")
    print(f"Puzzle B: {puzzle_b(data)}")