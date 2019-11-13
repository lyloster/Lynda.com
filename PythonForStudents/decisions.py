#add numbers greater than five to a new list
numbers = [1,2,3,4,5,6,7,8,9,10]
numbersGreaterThanFive = []

for i in numbers:
	#parenthesis are not needed
	if (i > 5):
		numbersGreaterThanFive.append(i)

print(numbersGreaterThanFive)


#check string equality
a = "foo"
b = "foos"
print(a==b)

for i in numbers:
	if (i == 4):
		print("4 is in the list of numbers")
	if (i == 11):
		print("11 is not in the list of numbers")


print("11 is not in the list of numbers")
