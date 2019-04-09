#Class review

class Customer:
    #CONSTRUCTOR
    def __init__(self,ID,Fname,Lname,Address,City,State,Zip,Phone):
        self.firstName=Fname
        self.lastName=Lname
        self.ID=ID
        self.Address=Address
        self.City = City
        self.State=State
        self.ZipCode= Zip
        self.PhoneNo= Phone
        self.purchases =[]
        self.total = 0


    #Parameters should be the items required to make the class.
    #ACCESSOR METHODS
    def getFname (self):
        return self.firstName
    def getLname (self):
        return self.lastName
    def getID (self):
        return self.ID
    def getAddress(self):
        Address = self.Address + "\n" + self.City + ","+ self.State+ " " + self.ZipCode
        return Address
    def getStreet(self):
        return self.Address
    def getCity(self):
        return self.City
    def getState(self):
        return self.State
    def getZipCode(self):
        return self.ZipCode
    def getPhoneNumber (self):
        return self.PhoneNo
    def getPurchases (self):
        output=""
        for i in self.purchases:
            output = output + str(i) + "\n"
        return output
    #def newCustomer (self,customer):
    
    def getTotal (self):
        return self.total
    
    #MUTATOR METHODS
    def setAddress (self,Address,City,State,Zip):
        self.Address = Address
    def addPurchase (self,purchase):
        self.purchases.append(purchase)
        self.total = self.total + purchase.getTotal()
    def setPhoneNo (self,Phone):
        self.PhoneNo = Phone
    def removePurchase (self,purchase):
        self.purchases.remove(purchase)
        self.total = self.total + purchase.getTotal()
    def setZipCode (self, Zip):
        self.ZipCode = Zip
    def setFirstName (self,Fname):
        self.firstName = Fname
    def setLastName (self,Lname):
        self.lastName = Lname
    def changeAddress(self, Address, City, State, Zip):
        self.Address = address
        self.City = city
        self.State = state
        self.Zip = zipcode

    def __str__(self):
        return "Customer ID: " + self.ID + "\nFirst Name:" + self.firstName + \
               "\nLast Name:" + self.lastName + "\nAddress:" + self.getAddress()+\
               "\nPhone: " + self.PhoneNo + "\nTotal: " + str(self.total)
        













