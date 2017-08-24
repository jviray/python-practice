"""
Write a function that takes a string and returns the number of vowels
in the string. You may assume that all the letters are lower cased.
You can treat "y" as a consonant.

Difficulty: easy.
"""

def count_vowels(string):
	vowels = ['a', 'e', 'i', 'o', 'u']
	count = 0

	for letter in string:
		if letter.lower() in vowels:
			count += 1

	return count

print(count_vowels('JONATHAN VIRAY'))