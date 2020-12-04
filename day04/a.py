#!/usr/bin/python3

import ast
import re

def load_input(path):
    with open(path, "r") as file:
        data = [x.replace("\n", " ") for x in file.read().split("\n\n")]
    return data

def puzzle_a():
	filtered = [x for x in data if len(x.split()) == 8]
	second_case = [x for x in data if len(x.split()) == 7 and "cid:" not in x]
	filtered.extend(second_case)
	return filtered

def puzzle_b(filtered):
	dict_list = [ast.literal_eval("{'%s'}" % x.replace(":", "':'").replace(" ", "', '")) for x in filtered]
	return sum(puzzle_b_requirements(x) for x in dict_list)

def puzzle_b_requirements(d):
	hcl_regex = "^#[0-9a-f]{6}$"
	pid_regex = "^[0-9]{9}$"
	eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
	req_tuple = (1920 <= int(d['byr']) <= 2002,
				2010 <= int(d['iyr']) <= 2020,
				2020 <= int(d['eyr']) <= 2030,
				height_filter(d['hgt']),
				bool(re.search(hcl_regex, d['hcl'])),
				d['ecl'] in eye_colors,
				bool(re.search(pid_regex, d['pid']))
				)
	return all(req_tuple)

def height_filter(height):
	if "cm" in height:
		return 150 <= int(re.search("\d+", height).group()) <= 193
	elif "in" in height:
		return 59 <= int(re.search("\d+", height).group()) <= 76

if __name__ == '__main__':
	data = load_input("./input")
	puzzle_a_output = puzzle_a()
	puzzle_b_output = puzzle_b(puzzle_a_output)
	print(f"Puzzle A: {len(puzzle_a_output)}")
	print(f"Puzzle B: {puzzle_b_output}")

