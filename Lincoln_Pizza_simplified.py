# define the class Order and constuctor
class Order:
    def __init__(self, member, size, drink, topping):
        self.memberStatus = member
        self.pizzaSize = size
        self.pizzaDrink = drink
        self.pizzaTopping = topping
# define the methods (within the class) to calculate the cost of each part
    def getPizzacost(self):
        if self.pizzaSize == "L":
            return 15.00
        elif self.pizzaSize == "M":
            return 12.00
        else:
            return 10.00

    def getDrinkcost(self):
        if self.pizzaDrink == "Fizz":
            return 5.00
        elif self.pizzaDrink == "Coffee":
            return 4.50
        elif self.pizzaDrink == "Cappuccino":
            return 5.50
        else:
            return 3.00
    
    def getToppingcost(self):
        return len(self.pizzaTopping) * 1.00

# define the method to calculate the total cost
    def getpizzaTotalcost(self):
    # set the initial total cost to 0.00
        total = 0.00
    # add the cost of the pizza, drink and toppings to the total
        total = self.getPizzacost() + self.getDrinkcost() + self.getToppingcost()
    # if member status is true, then apply 10% discount
        if (self.memberStatus):
            total = total * 0.9
        gst = total * 0.15
        total = total + gst
        return total

# define the driver program to test the methods
myOrder = Order(True, "L", "Fizz", ["Extra Cheese", "Pepperoni"])
print(myOrder)
print("The total cost of my pizza order is: " + "$" + str(myOrder.getpizzaTotalcost()))
    