class Item:
    def __init__(self,productID,productName,productPrice):
        self.price = productPrice
        #self.value = Value
        self.name = productName
        self.ProductID = productID
        self.items =[]
    #ACCESSORS
    def getproductName (self):
        return self.name
    def getproductID (self):
        return self.ProductID
    def getPrice (self):
        return self.prices
    #MUTATORS
    def setproductID (self):
        self.ProductID = newID
    def increasePrice (self,productPrice):
        self.price = price + Value
    def reducePrice (self,productPrice):
        self.price = price - Value
    def setproductName(self, newName):
        self.Name = newName
    def setPrice(self, newPrice):
        self.price = newPrice

    def __str__(self):
        return "Product ID: " + self.ProductID + "\nName: " + self.name + \
               "\nPrice: " + str(self.price) 


        
