'''
Project: Sal's Shipping

Sal runs the biggest shipping company in the tri-county area, Sal's Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

In this project, you'll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal's Shippers has several different options for a customer to ship their package:

Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you aren't charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
'''



weight = 4.8

#Ground Shipping
if weight <= 2:
  cost = 20 + (1.5 * weight)
elif weight > 2 and weight <= 6:
  cost = 20 + (3 * weight)
elif weight > 6 and weight <= 10:
  cost = 20 + (4 * weight)
else:
  cost = 20 + (4.75 * weight)
print("Cost for ground shipping is:",cost)

#Ground Shipping Premium (GSP)
cost_GSP = 125
print("Cost for ground shipping premium is:", cost_GSP)

#Drone Shipping (DS)
if weight <= 2:
  cost_DS = 4.5 * weight
elif weight > 2 and weight <= 6:
  cost_DS = 9 * weight
elif weight > 6 and weight <= 10:
  cost_DS = 12 * weight
else:
  cost_DS = 14.25 * weight
print("Cost for drone shipping is:",cost_DS)