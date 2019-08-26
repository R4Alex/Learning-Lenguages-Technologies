import re


def search(patterns, text):
	for pattern in patterns:
		print(re.findall(pattern, text))


# Character set
text = "hala hela hila hola hula"
patterns = ['h[aio]la', 'h[aeiou]']
search(patterns, text)
print()



text = "haala heeela hiiiila hooooola huuuuuula"
patterns = ['h[ae]la', 'h[ae]*la', 'h[io]{3,9}la']
search(patterns, text)
print()

# exclusion
text = "hala hela hila hola hula"
patterns = ['h[o]la', 'h[^o]la']
search(patterns, text)
print()

# ranges 
text = "hola h0la Hola mola m0lla M0la sdZd"
patterns = ['h[a-z]la', 'h[0-9]la', '[A-z]{4}', '[A-z0-9]{3}']
search(patterns, text)
print()

# Escape Characters
'''
\d numeric
\D no numeric
\s blank space
\S mo blank space
\W alphanumerioc
\W no alphanumeric
'''

text = "Este curso de pyhton 3 se publico en el año 2016"
patterns = [r'\d', r'\d+', r'\D', r'\D+', r'\s', r'\S', r'\S+', r'\w', r'\w+', r'\W+']
search(patterns, text)
print()
