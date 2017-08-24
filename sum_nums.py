"""
Write a function that takes in an integer `num` and returns the sum of
all integers between zero and num, up to and including `num`.

Difficulty: easy.
"""

def sum_nums(num):
	sum = 0
	for i in range(num + 1):
		sum += i

	return sum

print(sum_nums(5))