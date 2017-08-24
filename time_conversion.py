"""
Write a function that will take in a number of minutes, and returns a
string that formats the number into `hours:minutes`. Ex: time_conversion(120)
will return '2:00'.

Difficulty: easy.
"""

def time_conversion(minutes):
	hours = 0

	while minutes >= 60:
		hours += 1
		minutes -= 60

	if minutes < 10:
		minutes = "0" + str(minutes)
	else:
		minutes = str(minutes)

	return str(hours) + ":" + minutes

print(time_conversion(150))