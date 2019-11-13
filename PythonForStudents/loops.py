pizza_toppings = ["cheese", "pepperoni", "pineapple"]
print(pizza_toppings)

#pick a variable name representative of the elemnt you're working with
for topping in pizza_toppings:
	message = f"I would like to have {topping} on my pizza"
	print(topping)
	print(message)


myNumbers = [1,2,3]
mySquareNumbers = []
for number in myNumbers:
	mySquareNumbers.append(number*number)
print(mySquareNumbers)

#print even numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
	if(number%2==0):
		print(number)

