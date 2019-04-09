class Purchase:
    def __init__(self,receiptID, customerID):
        self.PurchaseID = receiptID
        self.customerID =customerID
        self.items = []
        self.total = 0
        
    #ACCESSORS    
    def getreceiptID (self):
        return self.PurchaseID
    def getTotal (self):
        return self.total
    def getItems (self):
        return self.items
    def getcustomerID(self):
        return self.customerID
    #MUTATORS
    def addItem  (self,item):
        self.items.append(item)
        self.total = self.total + item.getPrice()
    def removeItem (self,item):
        self.items.remove(item)
        self.total = self.total - item.getPrice()
    def setID(self, receiptID):
        self.PurchaseID = receiptID
    


    def __str__(self):
        output = ""
        output = output + "Receipt ID: " +  self.PurchaseID + "\n"
        
        for i in self.items:
            output = output + str(i) + "\n"

        return output
