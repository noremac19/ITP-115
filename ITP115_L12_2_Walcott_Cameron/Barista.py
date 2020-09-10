# Cameron Walcott, cwalcott@usc.edu
# ITP 115, Spring 2020
# Lab 12-2

from Coffee import Coffee

class Barista(object):
    MAX_ORDERS = 5

    def __init__(self,name):
        self.name = name
        self.orders = []

    def takeOrder(self):
        print("Hello, my name is",self.name,"and I am your barista.")
        desc = input("What drink do you want? ")
        size = input("What size would you like? ")
        customer = input("What is your name?: ")
        order = Coffee(size,desc,customer)
        self.orders.append(order)
        print(order)

    def isAcceptingOrders(self):
        if len(self.orders) < Barista.MAX_ORDERS:
            return True
        else:
            return False
    def makeDrinks(self):
        for drink in self.orders:
            drink.setCompleted()
            print('\t',drink)
        self.orders = []

    def __str__(self):
        msg = "Barista: " + self.name
        return msg