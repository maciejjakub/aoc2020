#!/usr/bin/python3

from itertools import combinations
import numpy as np

def load_input(path):
	with open(path, "r") as file:
		data = list(map(int, file.read().split()))
	return data

def puzzle_a():
	for i in data:
		for j in data:
			if i + j == 2020:
				print(f"The numbers are {i}, {j} and the answer is {i * j}")
				return None

def puzzle_alt(count):
	for i in combinations(data, count):
		if sum(i) == 2020:
			print(f"The numbers are {i} and the answer is {np.prod(i)}")

def puzzle_b():
	for i in data:
		for j in data:
			for k in data:
				if i + j + k == 2020:
					answer = i * j * k
					print(f"The numbers are {i}, {j}, {k} and the answer is {i * j * k}")
					return None
def puzzle_b_alt():
	puzzle_alt(3)

if __name__ == '__main__':
	data = load_input("./input")
	puzzle_a()
	# puzzle_b()
	puzzle_alt(2)
	puzzle_b_alt()
