import re 


def search(patterns, text):
	for pattern in patterns:
		print(re.findall(pattern, text))


text = "hla hola hoola hooola hoooooola"
patterns = ['hla', 'hola', 'hoola']
search(patterns, text)
print()

# meta character *
patterns = ['ho', 'ho*', 'ho*la', 'hu*la']
search(patterns, text)
print()

#meta character +
patterns = ['ho*', 'ho+']
search(patterns, text)
print()

# meta character ? one or no one letter on left
patterns = ['ho*', 'ho?', 'ho?la']
search(patterns, text)
print()

#repetitions and ranges 
patterns = ['ho{0}la', 'ho{3}la', 'ho{0,2}la']
search(patterns, text)
print()
