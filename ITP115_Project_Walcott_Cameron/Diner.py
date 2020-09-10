from MenuItem import MenuItem

class Diner(object):
    # create class variable
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]
    # define methods
    def __init__(self,name):
        self.name = name
        self.order = []
        self.status = 0

    # returns name of customer
    def getName(self):
        return self.name

    # sets name of customer
    def setName(self,nname):
        self.name = nname

    # returns customer's order
    def getOrder(self):
        return self.order

    # sets customers order
    def setOrder(self,norder):
        if len(self.order) == 0:
            self.order = [norder]
        else:
            self.order.append(norder)

    # returns integer of status
    # determines status of customer (seated,ordering,eating,paying,leaving)
    def getStatusInt(self):
        return self.status

    # returns string which is the customers status
    # based on index returned by getStatusInt
    def getStatus(self):
        return self.STATUSES[self.status]

    # sets customer status
    def setStatus(self,nstatus):
        self.status = int(nstatus)

    # updates customer status
    def updateStatus(self):
        self.status += 1

    # adds menu object to order list
    def addtoOrder(self,menuObject):
        self.order.append(menuObject)

    # prints order - menu objects added to order list are printed
    def printOrder(self):
        print(self.getName()+" has ordered:")
        for item in self.order:
            if item != None:
                print(item)

    # calculates meal cost based on price of each food in order
    def calculateMealCost(self):
        cost = 0.0
        for item in self.getOrder():
            cost += float(item.getPrice())
        return cost
    
    # Prints statement that declares the status of each customer
    def __str__(self):
        msg = "Diner " + self.getName() + " is currently " + self.getStatus()
        return msg
