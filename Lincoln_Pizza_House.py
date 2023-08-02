# define the class
class Pizza:
        # define the class constructor
    def __init__(self, pizzaSize, pizzaPrice):
        # define the class attributes
        self.Psize = pizzaSize
        self.Pprice = pizzaPrice

class Topping:
    def __init__(self, toppingType, toppingPrice):
        self.Ttype = toppingType
        self.Tprice = toppingPrice


class Drink:
    def __init__(self, drinkType, drinkPrice):
        self.Dtype = drinkType
        self.Dprice = drinkPrice

class Customer:
    def __init__(self, customerName, customerPhone, customerMember=False):
        self.Cname = customerName
        self.Cphone = customerPhone
        self.Cmember = customerMember

'''define the class OrderItem: this represents a specific item in an order,this means we can create a list
of items within the Order Class which makes it easier to manage and track the various items in the order'''
class OrderItem:
    def __init__(self, orderItem, orderQuantity):
        self.item=orderItem
        self.quantity=orderQuantity

'''define the class Order: this represents the overall order by a customer, 
its purpose to encapsulate all the relevant information to a specific order'''
class Orders:
    def __init__(self, orderID, orderDate, orderTime, orderType, orderStatus, orderTotal):
        self.orderID = orderID
        self.orderDate = orderDate
        self.orderTime = orderTime
        self.orderType = orderType
        self.orderStatus = orderStatus
        self.orderTotal = orderTotal
        self.items = []
        '''define the method of the class - add item - the add item method will add an item to the list items
        above - this is a list of objects of type OrderItem ''' 
    def add_item(self, item, quantity):
        self.items.append(OrderItem(item, quantity))

# define the lists of objects
pizzaList = [
Pizza("Small", 10.00),
Pizza("Medium", 12.00),
Pizza("Large", 14.00)]

toppingList = [
Topping("Extra Cheese", 1.00),
Topping("Pepperoni", 1.00),
Topping("Bacon", 1.00),
Topping("Seafood", 1.00),
Topping("Vegetables", 1.00)]

drinkList   = [
Drink("Fizzy Drink", 1.00),
Drink("Regular Coffee", 1.50),
Drink("Cappuccino", 1.50),
Drink("Tea", 2.00)]

def create_order(pizza, toppings, drink):
    total_cost = pizza.Pprice
    order_items = [OrderItem(pizza, 1)]
    for topping in toppings:
        total_cost += topping.Tprice
        order_items.append(OrderItem(topping, 1))
    for drink in drink:
        total_cost += drink.Dprice
        order_items.append(OrderItem(drink, 1))
    new_order = Orders(1, "2020-10-01", "12:00", "Delivery", "Complete", total_cost)
    new_order.items = order_items

    return new_order

print("My order cost: $" + str(create_order(pizzaList[0], [toppingList[0], toppingList[1]], [drinkList[0]]).orderTotal))

myOrders = []
myOrders.append(Orders(1, "2020-10-01", "12:00", "Delivery", "Complete", 25.00))
myOrders.append(Orders(2, "2020-10-02", "12:00", "Delivery", "Complete", 25.00))

from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
