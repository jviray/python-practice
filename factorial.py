"""
Write a function that takes an integer `n` as an input; 
it should return n*(n-1)*(n-2)*...*2*1. Assume n >= 0.

As a special case, `factorial(0) == 1`.

Difficulty: easy.
"""

def factorial(n):
	factorial = 1
	if n >= 1:
		for i in range(2, n + 1):
			factorial *= i

	return factorial

print(factorial(7))