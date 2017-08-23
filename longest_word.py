"""
Write a function that takes in a string. Return the longest word in
the string. You may assume that the string contains only letters and
spaces (no numbers).

You may use the String `split` function to aid you in your quest.

Difficulty: easy.
"""

def longest_word(sentence):
	longest_word = ""
	each_word = sentence.split()
	for word in each_word:
		if len(word) >= len(longest_word):
			longest_word = word 
	return longest_word

print(longest_word("Hello my name is Jonathan Viray"))