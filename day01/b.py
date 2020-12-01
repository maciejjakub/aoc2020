#!/usr/bin/python3

with open("input", "r") as file:
	data = list(map(int, file.read().split()))

for i in data:
	for j in data:
		for k in data:
			if i + j + k == 2020:
				answer = i * j * k
				print(f"The numbers are {i}, {j}, {k} and the answer is {answer}")
				quit()