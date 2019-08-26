#we can make comparasions without and if theres an element in commun
print(1 < 2 and 2 < 3)
#True
print(1 < 2 < 3)
#True

print(3 > 2 > 1)
#True

#however, this is not the same, because this comparision
#compares each minimum expresion\
print((3 > 2) and (2 > 1))
#True
print((3 > 2 ) > 1)
#False

# Sometimes this is going to change a little the logic
number = 39

if number >= 0 and number <=100:
	print("The number {} is between 0 and 100".format(number))
else:
	print("The number {} is not between 0 and 100".format(number))


# copmparasion on ans specific "direction"
if 0 <= number <= 100:
	print("The number {} is between 0 and 100".format(number))
else:
	print("The number {} is not between 0 and 100".format(number))

