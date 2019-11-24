pizzaTopings = ["cheese", "mushrooms", "pineapple"]
print("We have the following toppings:")

for topping in pizzaTopings:
	if (topping == "cheese"):
		print(f"{topping} (free)")
	elif (topping == "pineapple"):
		print(f"{topping} Please don't ask again")
	else:
		print(f"{topping} ($1)")

