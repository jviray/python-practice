""" 
Write a function that will take a stirng as an input, and return a new string
with the same letters in reverse order.

Don't use the String's reverse function.

Difficulty: Easy
"""

def reverse(word):
	reversed_word = ""
	word_length = len(word)
	for i in range(1, word_length + 1):
		reversed_word += word[-i]
	return reversed_word

print(reverse("Jonathan"))