# 1
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']; 

# 2
prices = [2, 6, 1, 3, 2, 7, 2]

# 3, 4
num_pizzas = len(toppings)


# 5, 6
pizzas = list(zip(prices, toppings))
# print(pizzas)

# 7
pizzas.sort()
# print(pizzas)

# 8
cheapest_pizza = pizzas[0]
# print(cheapest_pizza)

# 9
priciest_pizza = pizzas[-1]
print(priciest_pizza)

# 10, 11
three_cheapest = pizzas[:3]
print(three_cheapest)

# 12
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)