#Expected output
#Welcome to Julia's Pizzeria
#Our Available Toppings are:
#Cheese (Free)
#Pepperoni ($1 Extra)

pizzaToppings = ["cheese", "pepperoni"]

#change topping names to Title case
def formatTopping (topping):
	if (topping == "cheese"):
		return f"{topping.title()} (Free)"
	else:
		return f"{topping.title()}  ($1 Extra)"

#Check if the formatTopping function is working properly
print(formatTopping("cheese") == "Cheese (Free)")


def printMenu(toppings):
	print("Welcome to Julie's Pizzeria")
	print("Our available toppings are:")
	for topping in toppings:
		print(formatTopping(topping))

printMenu(pizzaToppings)