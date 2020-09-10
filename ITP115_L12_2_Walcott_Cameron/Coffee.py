# Cameron Walcott, cwalcott@usc.edu
# ITP 115, Spring 2020
# Lab 12-2

class Coffee(object):
    statuses = ["ordered","completed"] #attribute: variable stored within an object

    def __init__(self,drinkSize,description,customerName): #constructors: define what attributes will exist within an object
        self.size = drinkSize
        self.desc = description
        self.customer = customerName
        self.indexStatus = 0

    def setCompleted(self):
        self.indexStatus = 1

    def __str__(self):
        info = self.size + " " + self.desc + " for " + self.customer
        info += " ("+Coffee.statuses[self.indexStatus]+")"
        return info