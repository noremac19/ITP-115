from Menu import Menu
from Diner import Diner

class Waiter(object):
    # define methods
    def __init__(self,menuObject):
        self.menu = menuObject
        self.diners = []

    # adds diner object to list of diners
    def addDiner(self,dinerObject):
        self.diners.append(dinerObject)

    # returns num of diners
    def getNumDiners(self):
        return len(self.diners)

    # prints diner statuses
    def printDinerStatuses(self):
        # makes an array for each status
        one = []
        two = []
        three = []
        four = []
        five = []
        # adds name of each diner to the corresponding array
        # matching their status
        for item in self.diners:
            if item.status == 0:
                one.append(item.name)
            elif item.status == 1:
                two.append(item.name)
            elif item.status == 2:
                three.append(item.name)
            elif item.status == 3:
                four.append(item.name)
            elif item.status == 4:
                five.append(item.name)

        # Prints statement telling the status of each diner in the restaurant
        # Takes into account if more than one diner has the same status
        print("Diners who are seated:")
        for ind in one:
            print('\t', "Diner", ind, "is currently seated")

        print("Diners who are ordering:")
        for ind in two:
            print('\t', "Diner", ind, "is currently ordering")

        print("Diners who are eating:")
        for id in three:
            print('\t', "Diner", id, "is currently eating")

        print("Diners who are paying:")
        for id in four:
            print('\t', "Diner", id, "is currently paying")

        print("Diners who are leaving:")
        for id in five:
            print('\t', "Diner", id, "is currently leaving")


    def takeOrders(self):
        for item in self.diners:
            # checks for diner status "ordering"
            if item.getStatus() == Diner.STATUSES[1]:
                # loops a range of 4 because there are 4 menu item types
                for ind in range(4):
                    t = self.menu.MENU_ITEM_TYPES[ind]
                    self.menu.printMenuItemsByType(t)
                    true  = True
                    # error checking loop
                    # prompts user until correct/permissible input is made
                    while true:
                        selection = int(input("Please select an item to order by selecting its number: "))
                        # user inputs a permissible input on first attempt
                        if selection >= 1 and selection <= self.menu.getNumMenuItemsByType(t):
                            item.setOrder(self.menu.getMenuItem(t,selection))
                            true = False
                        else:
                            # user inputs an impermissible input on first attempt
                            print("Invalid input, please try again!")
                            end = 0
                            cont = True
                            # error checking loop begins
                            # Loops until a permissible input is entered
                            while cont:
                                selection = int(input("Please select an item to order by selecting its number: "))
                                if selection >= 1 and selection <= self.menu.getNumMenuItemsByType(t):
                                    item.setOrder(self.menu.getMenuItem(t, selection))
                                    end = 1
                                    cont = False
                                else:
                                    print("Invalid input, please try again!")
                            if end == 1:
                                true = False
                # prints order (if there is an order)
                if item.getOrder() != []:
                    print(item.printOrder())

    # calculates cost of customer's order and prints cost
    def ringUpDiners(self):
        cost = 0.0
        for item in self.diners:
            if item.getStatus() == "paying":
                cost += item.calculateMealCost()
                print(item.getName() + ", your meal costs " + "$" + str(cost))

    # checks if diner status is "leaving"
    # prints statement for diners that are leaving
    def removeDoneDiners(self):
        for item in self.diners:
            if item.getStatus() == "leaving":
                print(item.getName() + ", thank you for dining with us! Come again soon!")

        # removes diner from list of diner objects if status of diner is "leaving"
        for num in range(self.getNumDiners()-1,-1,-1):
            if self.diners[num].getStatus() == Diner.STATUSES[4]:
                del self.diners[num]

    # moves diners through checkpoints within statuses/restaurant procedures
    # updates status of diners and advances the diners
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for item in self.diners:
            item.updateStatus()
