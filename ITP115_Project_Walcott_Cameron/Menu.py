from MenuItem import MenuItem

class Menu(object):

    MENU_ITEM_TYPES = ["Drink","Appetizer","Entree","Dessert"]
    # define methods
    def __init__(self,fileName="menu.csv"):
        # creates dictionary and makes the keys the types of foods
        self.menuItemDictionary = {Menu.MENU_ITEM_TYPES[0]:[],Menu.MENU_ITEM_TYPES[1]:[],Menu.MENU_ITEM_TYPES[2]:[],Menu.MENU_ITEM_TYPES[3]:[]}
        self.file = fileName
        ifile = open(self.file, "r")
        # reads menu.csv file
        for line in ifile:
            # separates each line of the file into a list
            object = line.strip()
            object = object.split(",")
            # Comments for if-else statement chain:
            #   checks and matches the first index of the list with the MENU_ITEMS_TYPE list
            #   assigns rest of values in list
            #   appends MenuItem object to the menuItemDictionary
            #   using the corresponding key found by conditional if statement
            if object[1] == Menu.MENU_ITEM_TYPES[0]:
                namef = str(object[0])
                typef = str(object[1])
                pricef = float(object[2])
                descf = str(object[3])
                self.menuItemDictionary[object[1]].append(MenuItem(namef,typef,pricef,descf))
            elif object[1] == Menu.MENU_ITEM_TYPES[1]:
                namef = str(object[0])
                typef = str(object[1])
                pricef = float(object[2])
                descf = str(object[3])
                self.menuItemDictionary[object[1]].append(MenuItem(namef,typef,pricef,descf))
            elif object[1] == Menu.MENU_ITEM_TYPES[2]:
                namef = str(object[0])
                typef = str(object[1])
                pricef = float(object[2])
                descf = str(object[3])
                self.menuItemDictionary[object[1]].append(MenuItem(namef,typef,pricef,descf))
            elif object[1] == Menu.MENU_ITEM_TYPES[3]:
                namef = str(object[0])
                typef = str(object[1])
                pricef = float(object[2])
                descf = str(object[3])
                self.menuItemDictionary[object[1]].append(MenuItem(namef,typef,pricef,descf))
        ifile.close()
    # returns menuItem object
    def getMenuItem(self,typeItem,indexItem):
        objectList = self.menuItemDictionary[typeItem]
        obj = objectList[indexItem-1]
        return obj
    # prints all menu items for a single type of food *******************
    def printMenuItemsByType(self,typeItem):
        print(typeItem+"s:")
        list = self.menuItemDictionary[typeItem]
        num = 1
        for item in list:
            print('\t'+str(num)+")",item.nme)
            print('\t'+'\t'+"-",item.getDescription())
            num += 1
    # returns number of menu items for a specific type
    def getNumMenuItemsByType(self,typeItem):
        list = self.menuItemDictionary[typeItem]
        return len(list)

