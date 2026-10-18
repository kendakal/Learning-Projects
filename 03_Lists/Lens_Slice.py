'''
Project: Len's Slice
You work at Len's Slice, a new pizza joint in the neighborhood. 
You are going to use your knowledge of Python lists to organize some of your sales data.
'''


# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizzas!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

pizza_and_prices_sorted = sorted(pizza_and_prices)
print(pizza_and_prices_sorted)
cheapest_pizza = pizza_and_prices_sorted[0]
priciest_pizza = pizza_and_prices_sorted[-1]

pizza_and_prices_sorted.pop()
print(pizza_and_prices_sorted)

pizza_and_prices_sorted.insert(3, [2.5, "peppers"])

three_cheapest = pizza_and_prices_sorted[:3]
print("The three cheapest pizza are", three_cheapest)