import re

text = "on this string there is a magic word"

result = re.search('magic', text)

if result is not None:
	print("the word has been found")
else:
	print("The word hasn't been found")


print(result.start())
print(result.end())
print(result.span())
print(result.string)

# does text start with
text = "hello world"
result = re.match("hello", text)
print(result)

# split
text = "let's split this string"
result = re.split(' ', text)
print(result)


text = "hello boy"
result = re.sub('boy', "girl", text)
print(result)


text = "hello bye hello hello"
result = re.findall("hello", text)
print(result)
print(len(result))


text = "hello bye hola adios"
result = re.findall("(hello|hola)", text)
print(result)