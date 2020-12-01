#!/usr/bin/python3

from itertools import combinations
import numpy as np

def load_input(path):
	with open(path, "r") as file:
		data = list(map(int, file.read().split()))
	return data

def puzzle(count):
	for i in combinations(data, count):
		if sum(i) == 2020:
			print(f"The numbers are {i} and the answer is {np.prod(i)}")

if __name__ == '__main__':
	data = load_input("./input")
	print("Puzzle A:")
	puzzle(2)
	print("Puzzle B:")
	puzzle(3)
