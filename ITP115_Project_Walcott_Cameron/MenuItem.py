
class MenuItem(object):
    # define methods
    def __init__(self,name,ftype,price,description):
        self.nme = str(name)
        self.ty = str(ftype)
        self.prc = float(price)
        self.des = str(description)

    # returns name of food
    def getName(self):
        return self.nme

    # sets name of food
    def setName(self,nname):
        self.nme = nname

    # returns type of food
    def getType(self):
        return self.ty

    # sets type of food
    def setType(self,ntype):
        self.ty = ntype

    # returns price of food
    def getPrice(self):
        return self.prc

    # sets price of food
    def setPrice(self,nprice):
        self.prc = nprice

    # returns description of food
    def getDescription(self):
        return self.des

    # sets description of food
    def setDescription(self,ndescription):
        self.desc = ndescription

    # returns message printing each food and its attribute (name,price,type,description)
    def __str__(self):
        msg = self.getName() + " (" + self.getType() + "): $" + str(self.getPrice())
        msg += '\n' + '\t' + self.getDescription()
        return msg
