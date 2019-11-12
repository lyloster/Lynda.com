def pizzaName (topping):
	return (f"{topping.title()} Pizza")

pizza = pizzaName("cheese")
print(pizza)


def timesTwo(n):
	return n*2

print(timesTwo(2))


def introduceYourself(name, age):
	return(f"My name is {name} and I am {age} years old.")

introduction = introduceYourself("Mary", 24)
print(introduction)	