numbers = [1,2,3]
pizza_toppings = ["cheese", "pepperoni"]
mixed_list = [1, "cheese", 2, "pepperoni"]
list_of_lists = [[1,2], [6,4]]

#access individual element
print(pizza_toppings[0])

#from the end
print(pizza_toppings[-1])

#in python - out of bound errors
#lists are mutable

#length of list
print(len(pizza_toppings))

#at the end of the list
pizza_toppings.append("pineapple")

#at specific index
pizza_toppings.insert(0, "mushrooms")

#remove
del pizza_toppings[0]

#remove from the end of the list
pizza_toppings.pop()

#remove specific element, removes the first instance
pizza_toppings.remove("cheese")

print(pizza_toppings)

pizza_toppings = ["cheese", "cheese", "pepperoni"]
pizza_toppings.remove("cheese")

print(pizza_toppings)



