from Purchase import Purchase
from Customer import Customer
from Item import Item
from graphics import *
from Button import Button

class Store :
    def __init__(self, name):
        self.name = name
        self.customerList=[]
        self.itemList =[]
        self.purchaseList =[]
        self.revenue = 0
        self.dummyLists()
        self.createWin()
   

#ACCESSOR METHODS
#To get information

    def getName (self):
        return self.name
    def getRevenue (self):
        return self.revenue
    def getCustomerList(self):
        return self.customerList
    def getItemList(self):
        return self.itemList
    def getPurchaseList(self):
        return self.purchaseList
    def clicked (self,pt ):
        "Return true if button active and p is inside the button"
        return self.active and self.xmin <= pt.getX() <= self.xmax and self.ymin <= pt.getY() <= self.ymax

#MUTATOR METHODS
#To change information
    def setName(self, name):
        self.name = name
    def setRevenue (self, newRevenue):
        self.revenue = newRevenue
    
    
    
                                                     #CUSTOMER METHODS
   
    def addCustomer (self):

#Creates the addcustomer window.
        win = GraphWin ("New Customer",500,400)
        win.setBackground("Sky Blue")
#TEXT
        ID1 = Text(Point(150,20), "ID")
        ID1.setTextColor("White")
        ID1.draw(win)
        
        Fname1 = Text(Point(150,50),"First Name")
        Fname1.setTextColor("White")
        Fname1.draw(win)
        
        Lname1= Text(Point(150,80),"Last Name")
        Lname1.setTextColor("White")
        Lname1.draw(win)
        
        Address1 = Text(Point(150,110),"Street Address")
        Address1.setTextColor("White")
        Address1.draw(win)
        
        City1 = Text(Point(150,140),"City")
        City1.setTextColor("White")
        City1.draw(win)
        
        State1 = Text (Point(150,170),"State")
        State1.setTextColor("White")
        State1.draw(win)
        
        Zcode1 = Text(Point(150,200),"Zip Code")
        Zcode1.setTextColor("White")
        Zcode1.draw(win)
        
        Phone1 = Text(Point(150,230),"Phone Number")
        Phone1.setTextColor("White")
        Phone1.draw(win)
        


#Entry Points
        E1=Entry(Point(300,20), 20)
        E1.setFill("White")
        E1.draw(win)
        
        E2 = Entry(Point(300,50), 20)
        E2.setFill("White")
        E2.draw(win)
        
        E3 = Entry(Point(300,80), 20)
        E3.setFill("White")
        E3.draw(win)
        
        E4 = Entry(Point(300,110), 20)
        E4.setFill("White")
        E4.draw(win)
        
        E5 = Entry(Point(300,140), 20)
        E5.setFill("White")
        E5.draw(win)
        
        E6 = Entry(Point(300,170), 20)
        E6.setFill("White")
        E6.draw(win)
        
        E7 = Entry(Point(300,200), 20)
        E7.setFill("White")
        E7.draw(win)
        
        E8 = Entry(Point(300,230), 20)
        E8.setFill("White")
        E8.draw(win)
#BUTTONS
        Add = Button(win, Point(200,270),120,30,"Add")
        Add.activate()
        
        Back = Button(win, Point(400,270),120,30,"Back")
        Back.activate()
              
#LOOP
# specifies that while not the back button clicked, if the add button is clicked
# the parameters for a new customer object is created as variables and assigned to the text placed in the entry boxes
# which creates the "newCustomer" object thats added to the list.
        pt = win.getMouse()
        while not Back.clicked(pt):
            if Add.clicked(pt):
                ID = E1.getText()
                Fname = E2.getText()
                Lname = E3.getText()
                Address = E4.getText()
                City  = E5.getText()
                State = E6.getText()
                Zip = E7.getText()
                Phone = E8.getText()
                newCustomer = Customer(ID,Fname,Lname,Address,City,State,Zip,Phone)
                #adds new customer to list
                self.customerList.append(newCustomer)
                #prints new customer message in window
                CustAdded= Text(Point(250,350),"New Customer has been added.")
                CustAdded.setTextColor("Dark Blue")
                CustAdded.setSize(18)
                CustAdded.draw(win)
            pt = win.getMouse()
                 
        win.close()
               
                                                                #ITEM METHODS
    def addItem (self):
        win = GraphWin ("New Item",400,200)
        win.setBackground("Sky Blue")
#TEXT
        
        PId = Text (Point(100,50),"Product ID")
        PId.draw(win)
        PId.setTextColor("White")
        
        Iname = Text(Point(100,80), "Item Name")
        Iname.draw(win)
        Iname.setTextColor("White")
        
        Price = Text(Point(100,110),"Price")
        Price.draw(win)
        Price.setTextColor("White")
        
        
#ENTRY BOX
        E1 = Entry(Point(200,50), 10)
        E1.setFill("White")
        E1.draw(win)
        
        E2 = Entry(Point(200,80), 10)
        E2.setFill("White")
        E2.draw(win)
        
        E3 = Entry(Point(200,110), 10)
        E3.setFill("White")
        E3.draw(win)

        
#BUTTONS
        Add = Button(win, Point(150,170),70,30,"Add")
        Add.activate()
        
        Back = Button(win, Point(250,170),70,30,"Back")
        Back.activate()
#LOOP
# creates new item object and adds to list.
        pt = win.getMouse()
        while not Back.clicked(pt):
            if Add.clicked(pt):
                productID = E1.getText()
                productName = E2.getText()
                productPrice = E3.getText()
                newItem = Item (productID,productName,productPrice)
                #adds new item to list
                self.itemList.append(newItem)
                #prints message for item.
                ItemAdded= Text(Point(200,180),"New Item has been added.")
                ItemAdded.setTextColor("Dark Blue")
                ItemAdded.setSize(12)
                ItemAdded.draw(win)
            pt = win.getMouse()
        win.close()
                                   #PURCHASE METHODS

                
    def addPurchase (self):
         win = GraphWin ("Store",400,200)
         win.setBackground("Sky Blue")
#TEXT 
         ID1 = Text(Point(100,50), "Customer ID")
         ID1.draw(win)
         
         PId1 = Text (Point(100,80),"Product ID")
         PId1.draw(win)
         
##         ProdQ1 = Text(Point(95,110),"Product Quantity")
##         ProdQ1.draw(win)
##         
##         Price1 = Text(Point(100,140),"Price")
##         Price1.draw(win)

#ENTRY BOX

         E1 = Entry(Point(200,50), 10)
         E1.setFill("White")
         E1.draw(win)
         
         E2 = Entry(Point(200,80), 10)
         E2.setFill("White")
         E2.draw(win)
         
##         E3 = Entry(Point(200,110), 10)
##         E3.setFill("White")
##         E3.draw(win)
##         
##         E4 = Entry(Point(200,140), 10)
##         E4.setFill("White")
##         E4.draw(win)
         
#ADD & BACK BUTTON

         Add = Button(win, Point(150,150),70,30,"Add")
         Add.activate()
         
         Back = Button(win, Point(250,150),70,30,"Back")
         Back.activate()

         pt = win.getMouse()
#LOOP
         #loop for creating the new order.
         while not Back.clicked(pt):
             if Add.clicked(pt):
                receiptID= E1.getText()
                productID= E2.getText()
##                productQuantity = E3.getText()
##                Price = E4.getText()

                #prints message for completed order.
                PurchaseC= Text(Point(200,230),"Purchase Complete")
                PurchaseC.setTextColor("Dark Blue")
                PurchaseC.setSize(12)
                PurchaseC.draw(win)
                #creates a new purchase object
                newOrder= Purchase(receiptID)
                #adds order to the purchase list.
                self.purchaseList.append(newOrder)
         pt = win.getMouse()
         win.close()
     

              #REMOVE WINDOW: This window opens when remove button is clicked.
              #Contains mini windows where you can make selections of the object you'd like to delete.



    def Remove(self):
        win = GraphWin ("Delete",250,300)
        win.setBackground("Black")
        TRemove = Text (Point(115, 50)," What do you want to delete?")
        TRemove.setFill("Blue")
        TRemove.setStyle("bold")
        TRemove.setSize(12)
        TRemove.draw(win)
        
        CustomerB = Button(win, Point(125,90),100,30,"Customer")
        CustomerB.activate()
        ItemB = Button(win, Point(125,120),100,30,"Item")
        ItemB.activate()
        OrderB = Button(win, Point(125,150),100,30,"Receipt")
        OrderB.activate()
        BackB = Button(win, Point(125,190),100,30,"Back")
        BackB.activate()

        pt = win.getMouse()

#mini winows for deletion      
    
        if CustomerB.clicked(pt):
            win1 = GraphWin ("Customer Deletion", 400,200)
            win1.setBackground("Sky Blue")

            Remove1= Text(Point(200,50), "Enter Customer ID or Customer Name")
            Remove1.draw(win1)
            R1= Entry(Point(200,75), 20)
            R1.draw(win1)
            R1.setFill("White")
            BackB1=Button(win1, Point(100,120),70,30,"Back")
            BackB1.activate()
            RemoveB1 =Button(win1, Point(300,120),70,30,"Remove")
            RemoveB1.activate()

            pt = win1.getMouse()
            while not BackB1.clicked(pt):
                if RemoveB1.clicked(pt):
                        #checks if text entry is a string or int
                        #if string 
                        if (R1.getText().isdigit())== False:
                            #splits entry to get first & last name
                            Fname, Lname = R1.getText().split()
                            output = self.searchCustomerName(Fname, Lname)
                            
                            #prints output message into window
                            if output != False:
                                outputT = Text(Point(200,160), output.getFname()+ " " +output.getLname()+ "with ID number:" +" " + output.getID() + " " + "has been removed")
                                outputT.setSize(13)
                                outputT.setFill("Blue")
                                outputT.draw(win1)
                                self.customerList.remove(output)
                            else:
                                outputT = Text(Point(200,160), "Customer not found")
                                outputT.setSize(13)
                                outputT.setFill("Blue")
                                outputT.draw(win1)
                        #if int
                        elif (R1.getText().isdigit())== True :
                            ID = R1.getText()
                            output = self.searchCustomerID(ID)
                            #prints output message into window
                            if output != False:
                                outputT = Text(Point(200,160), output.getFname()+ " " +output.getLname()+ " " + "has been removed")
                                outputT.setSize(13)
                                outputT.setFill("Blue")
                                outputT.draw(win1)
                                self.customerList.remove(output)
                            else:
                                outputT = Text(Point(200,160), "Customer not found")
                                outputT.setSize(13)
                                outputT.setFill("Blue")
                                outputT.draw(win1)
                                               
                        pt = win1.getMouse()
                        
            win1.close()
            
        if ItemB.clicked(pt):
            win2 = GraphWin ("Item Deletion", 400,200)
            win2.setBackground("Sky Blue")

            Remove2 = Text(Point(200,50), "Enter Product ID or Product Name")
            Remove2.draw(win2)
            R2= Entry(Point(200,75), 20)
            R2.draw(win2)
            R2.setFill("White")
            BackB2=Button(win2, Point(100,120),70,30,"Back")
            BackB2.activate()
            RemoveB2 =Button(win2, Point(300,120),70,30,"Remove")
            RemoveB2.activate()

            pt = win2.getMouse()
            while not BackB2.clicked(pt):
                if RemoveB2.clicked(pt):
                    if (R2.getText().isdigit()) == False:
                        productName= R2.getText()
                        output = self.searchItemName(productName)
                        if output != False:
                            outputT = Text(Point(200,160), output.getproductName() + "with ID Number : "+" " + output.getproductID()+ " " +  "has been removed")
                            outputT.setSize(13)
                            outputT.setFill("Blue")
                            outputT.draw(win2)
                            self.itemList.remove(output)
                        else:
                            outputT = Text(Point(200,160), "Item not Found")
                            outputT.setSize(13)
                            outputT.setFill("Blue")
                            outputT.draw(win2)
                    elif (R2.getText().isdigit()) == True:
                        productID= R2.getText()
                        output = self.searchItemID(productID)
                        if output != False:
                            outputT = Text(Point(200,160), "The found item " + " " + output.getproductName() + " " + "has been removed.")
                            outputT.setSize(13)
                            outputT.setFill("Blue")
                            outputT.draw(win2)
                            self.itemList.remove(output)
                        else:
                            outputT = Text(Point(200,160), "Item not Found")
                            outputT.setSize(13)
                            outputT.setFill("Blue")
                            outputT.draw(win2)
                            
                        
                    pt = win2.getMouse()
                        
            win2.close()
            
            
        if OrderB.clicked(pt):
            win3 = GraphWin ("Purchase Delete", 400,200)
            win3.setBackground("Sky Blue")

            Remove3 = Text(Point(200,50), "Enter Receipt ID ")
            Remove3.draw(win3)
            R3= Entry(Point(200,75), 20)
            R3.draw(win3)
            R3.setFill("White")
            BackB3=Button(win3, Point(100,120),70,30,"Back")
            BackB3.activate()
            RemoveB3 =Button(win3, Point(300,120),70,30,"Remove")
            RemoveB3.activate()

            pt = win3.getMouse()
            while not BackB3.clicked(pt):
                if RemoveB3.clicked(pt):
                    receiptID = R3.getText()
                    output = self.removePurchase(receiptID)
                    outputT = Text(Point(100,160), "Purchase with receipt ID :" + " " + output.getreceiptID() + " " + "has been removed")
                    outputT.setSize(13)
                    outputT.setFill("Blue")
                    outputT.draw(win2)
                    self.purchaseList.remove(receiptID)
                    pt = win3.getMouse()
            win3.close()
            
                

        if BackB.clicked(pt):
            win.close()
            
        

                                                    #SEARCH WINDOW:             This window opens when search button is clicked on main window .
                                                                                #Contains sub-windows that help determine what exactly you want to look for.


    def Search(self) :
        win = GraphWin ("Search",250,300)
        win.setBackground("Black")

        TSearch = Text (Point(125, 50)," What are you looking for?")
        TSearch.setFill("Blue")
        TSearch.setStyle("bold")
        TSearch.setSize(12)
        TSearch.draw(win)
        
        CustomerB = Button(win, Point(125,90),100,30,"Customer")
        CustomerB.activate()
        ItemB = Button(win, Point(125,120),100,30,"Item")
        ItemB.activate()
        OrderB = Button(win, Point(125,150),100,30,"Receipt")
        OrderB.activate()
        BackB = Button(win, Point(125,190),100,30,"Back")
        BackB.activate()
        pt = win.getMouse()
    
        if CustomerB.clicked(pt):
            win1 = GraphWin ("Customer Search", 400,200)
            win1.setBackground("Sky Blue")

            Search = Text(Point(200,50), "Enter Customer ID or Customer Name")
            Search.draw(win1)
            S1= Entry(Point(200,75), 20)
            S1.draw(win1)
            S1.setFill("White")
            BackB1=Button(win1, Point(100,120),70,30,"Back")
            BackB1.activate()
            SearchB1 =Button(win1, Point(300,120),70,30,"Search")
            SearchB1.activate()
            
            pt = win1.getMouse()
            while not BackB1.clicked(pt):
                if SearchB1.clicked(pt):
#loop checks to see if the entry is an int or string data type. #method for checking is "isdigit()"
                    if (S1.getText().isdigit())== False:
                        Fname, Lname = S1.getText().split()
                        output= self.searchCustomerName(Fname, Lname)
                        if output != False:
                            outputT = Text(Point(200,160), output.getFname()+ " " +output.getLname()+ " " + "has ID number:" + " " + output.getID())
                            outputT.setSize(13)
                            outputT.setFill("Blue")
                            outputT.draw(win1)
                        else:
                            outputT = Text(Point(200,160), "Customer not found")
                            outputT.setSize(13)
                            outputT.setFill("Blue")
                            outputT.draw(win1)
                    elif (S1.getText().isdigit())== True :
                        ID = S1.getText()
                        output= self.searchCustomerID(ID)
                        if output != False:
                            outputT = Text(Point(200,160), output.getFname()+ " " +output.getLname()+ " " + "has been found")
                            outputT.setSize(13)
                            outputT.setFill("Blue")
                            outputT.draw(win1)
                        else:
                            outputT = Text(Point(200,160), "Customer not found")
                            outputT.setSize(13)
                            outputT.setFill("Blue")
                            outputT.draw(win1)
                pt = win1.getMouse()            
            win1.close()
            
    
        if ItemB.clicked(pt):
            win2 = GraphWin ("Item Search", 400,200)
            win2.setBackground("Sky Blue")

            Search = Text(Point(200,50), "Enter Product ID")
            Search.draw(win2)
            S2= Entry(Point(200,75), 20)
            S2.draw(win2)
            S2.setFill("White")
            BackB2=Button(win2, Point(100,120),70,30,"Back")
            BackB2.activate()
            SearchB2 =Button(win2, Point(300,120),70,30,"Search")
            SearchB2.activate()

            pt = win2.getMouse()
            while not BackB2.clicked(pt):
                if SearchB2.clicked(pt):
                    if (S2.getText().isdigit()) == False:
                        productName= S2.getText()
                        output = self.searchItemName(productName)
                        if output != False:
                            outputT = Text(Point(100,160), output.getproductName() + "has ID Number : "+" " + output.getproductID())
                            outputT.setSize(13)
                            outputT.setFill("Blue")
                            outputT.draw(win2)
                        else:
                            outputT = Text(Point(200,160), "Item not Found")
                            outputT.setSize(13)
                            outputT.setFill("Blue")
                            outputT.draw(win2)
                    elif (S2.getText().isdigit()) == True:
                        productID = S2.getText()
                        output = self.searchItemID(productID)
                        if output != False:
                            outputT = Text(Point(200,160), "The found item is " +" " + output.getproductName())
                            outputT.setSize(13)
                            outputT.setFill("Blue")
                            outputT.draw(win2)
                        else:
                            outputT = Text(Point(200,160), "Item not Found")
                            outputT.setSize(13)
                            outputT.setFill("Blue")
                            outputT.draw(win2)
                pt = win2.getMouse()
                        
            win2.close()
            
            
        if OrderB.clicked(pt):
            win3 = GraphWin ("Customer Search", 400,200)
            win3.setBackground("Sky Blue")

            Search = Text(Point(200,50), "Enter Receipt ID ")
            Search.draw(win3)
            S3= Entry(Point(200,75), 20)
            S3.draw(win3)
            S3.setFill("White")
            BackB3=Button(win3, Point(100,120),70,30,"Back")
            BackB3.activate()
            SearchB3 =Button(win3, Point(300,120),70,30,"Search")
            SearchB3.activate()

            pt = win3.getMouse()
            while not BackB3.clicked(pt):
                if SearchB3.clicked(pt):
                    receiptID = S3.getText()
                    output = self.searchReceiptID(receiptID)
                    outputT = Text(Point(100,160), "Purchase with receipt ID :" + " " + output.getreceiptID() + " " + "has been found")
                    outputT.setSize(13)
                    outputT.setFill("Blue")
                    outputT.draw(win2)
                            
                    pt = win3.getMouse()
            win3.close()
            

        if BackB.clicked(pt):
            win.close()
            


                                                        #SORT METHODS
    def sortCustomerID(self) :
#passnum is a random variable
#uses length of customer list to determine the starting item number , 0 - the end point number
# and the steps to take , like going backwards hence -1
#example , customerlenght is 6 (but because the first item is 0 "-1", so actual lenght is 5)
# the first item is item'0' hence - 0(middle)

        for passnum in range (len(self.customerList)-1,0,-1):
#for the items in the list going backwards, do the comparison
            for i in range (passnum):
#for the items in the list compare the initial customerID to the next customerID,
#if the initial is greater than next , then they switch positions by double assigning.
                if self.customerList[i].getID()> self.customerList[i+1].getID() :
                    self.customerList[i], self.customerList[i+1] = self.customerList[i+1], self.customerList[i]
    customerList = []

    def sortCustomerName (self):
        for passnum in range (len(self.customerList)-1,0,-1):
            for i in range (passnum):
                if self.customerList[i].getLname()  > self.customerList[i+1].getLname() :
                    self.customerList[i], self.customerList[i+1] = self.customerList[i+1], self.customerList[i]
                elif self.customerList[i].getLname() == self.customerList[i+1].getLname :
                    if self.customerList.getFname [i] > self.customerList.getFname [i+1]:
                        self.customerList[i], self.customerList[i+1] = self.customerList[i+1], self.customerList[i]

                    
    customerList = []

    def sortItemID (self):
        for passnum in range (len(self.itemList)-1,0,-1):
            for i in range (passnum):
                if self.itemList[i].getproductID() > self.itemList[i+1].getproductID() :
                    self.itemList[i], self.itemList[i+1] = self.itemList[i+1], self.itemList[i]
    itemList = []

    def sortItemName (self):
        for passnum in range (len(self.itemList)-1,0,-1):
            for i in range (passnum):
                if self.itemList[i].getproductName()> self.itemList[i+1].getproductName() :
                    self.itemList[i], self.itemList[i+1] = self.itemList[i+1], self.itemList[i]
    itemList = []

    def sortPurchaseID(self) :
        for passnum in range (len(self.purchaseList)-1,0,-1):
            for i in range (passnum):
                if self.purchaseList[i].getreceiptID() > self.purchaseList[i+1].getreceiptID() :
                    self.purchaseList[i], self.purchaseList[i+1] = self.purchaseList[i+1], self.purchaseList[i]
    purchaseList = []


                                                         #SEARCH METHODS
    def searchCustomerID(self , ID):

        self.sortCustomerID()
        first = 0
        last = len(self.customerList) - 1

        found = False

        while first <= last and not found :
            midpoint = (first + last)// 2
            
            if self.customerList[midpoint].getID() == ID:
                found = self.customerList[midpoint]
                #print(self.customerList[midpoint].getFname()+ " " + self.customerList[midpoint].getLname(),"has been found.") 
            else :
                if (ID < self.customerList [midpoint].getID()):
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        return found
        

    def searchCustomerName(self , Fname, Lname):
        self.sortCustomerName()
        first = 0
        last = len(self.customerList) - 1

        found = False

        while first <= last and not found :
            midpoint = (first + last)// 2
            
            if self.customerList[midpoint].getLname() == Lname:
                if self.customerList[midpoint].getFname() == Fname:
                    found = self.customerList[midpoint]
                    #print(self.customerList[midpoint].getFname()+ " " + self.customerList[midpoint].getLname(),"has been found.")
                else :
                    if (Fname < self.customerList[midpoint].getFname):
                        last = midpoint -1
                    else:
                        first = midpoint+1
            else:
                if (Lname < self.customerList [midpoint].getLname()):
                    last = midpoint - 1
                else:
                    first = midpoint + 1
                    
        return found

    def searchItemID (self, productID):
        self.sortItemID()
        first = 0
        last = len(self.itemList) - 1

        found = False

        while first <= last and not found :
            midpoint = (first + last)// 2
            
            if self.itemList[midpoint].getproductID() == productID:
                found = self.itemList[midpoint]
                #print(self.itemList[midpoint].getproductName())
            else :
                if (productID < self.itemList [midpoint].getproductID()):
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        return found

    def searchItemName (self, productName):
        self.sortItemName()
        first = 0
        last = len(self.itemList) - 1

        found = False

        while first <= last and not found :
            midpoint = (first + last)// 2
            
            if self.itemList[midpoint].getproductName == productName:
                found = self.itemList[midpoint].getproductName
                #print(self.itemList[midpoint].getproductName())
            else :
                if (productName < self.itemList [midpoint].getproductName()):
                    last = midpoint -1
                else:
                    first = midpoint+1
##            else:
##                print("Item not found")
        return found
    def searchReceiptID (self, receiptID):
        first = 0
        last = len(self.purchaseList) - 1

        found = False

        while first <= last and not found :
            midpoint = (first + last)// 2
            
            if self.purchaseList[midpoint].getreceiptID() == receiptID:
                found = self.purchaseList[midpoint].getreceiptID()
            else :
                if (ID < self.purchaseList [midpoint]):
                    last = midpoint -1
                else:
                    first = midpoint+1
        return found


                                                        #REMOVE METHODS
    def removeCustomerID (self,ID):
          Rcustomer = self.searchCustomerID(ID)

         if Rcustomer != False:
             self.customerList.remove(Rcustomer)
             #print (Rcustomer.getFname()+ " " + Rcustomer.getLname()," has been removed")
          else:
              Rcustomer == False


    def removeCustomerName (self, Lname , Fname):
        Rcustomer = self.searchCustomerName(Lname, Fname)

        if Rcustomer != False:
              self.customerList.remove(Rcustomer)
              #print ("Customer has been removed")
        else:
              Rcustomer = False

        

    def removeItemID (self,productID):
          Ritem = self.searchItemID(productID)

          if Ritem != False:
              self.itemList.remove(Ritem)
              #print ("Item has been removed")
           else:
             Rcustomer = False

          
        
    def removeItembyName (self,productName):
        Ritem = self.searchItemID(productName)

        if Ritem != False:
          self.itemList.remove(Ritem)
          #print ("Item has been removed")
        else:
          Rcustomer == False

        

    def removePurchase(self, receiptID):
        ROrder = self.searchReceiptID(receiptID)

        if ROrder != False:
          self.itemList.remove(Ritem)
          #print ("Order has been cancelled")
        else:
          Rcustomer == False

        

    
  
#fake list that creates a customer , item , and purchase object to prevent us from creating new ones all the time.
#has to  be initialized at the top before main window
    def dummyLists(self):
        self.customerList.append(Customer("0001", "Joshua","Ikeobi","206 Eagle Drive","Elizabethtown","KY","42701","270-325-6555"))
        self.customerList.append(Customer("0002", "Hayden", "Fentress", "512 Northern Way", "Fort Worth", "TX", "76153", "512-226-3542"))
        self.itemList.append(Item("567", "Bread" ,25.55 ))
        self.itemList.append(Item("568", "Milk" ,30.55 ))
        

    
      

    def createWin(self):
        win = GraphWin ("Store",350,350)
        win.setBackground("Black")

        Name = Text(Point(175,40)," WILDCAT ENT.")
        Name.setFill("Blue")
        Name.setStyle("bold")
        Name.setSize(20)
        Name.draw(win)
                    
        b1 = Button(win, Point(175,80),120,30,"New Customer")
        b1.activate ()
        b2 = Button(win, Point(175,110),120,30,"Item")
        b2.activate ()
        b3 = Button(win, Point(175,140),120,30,"Order")
        b3.activate ()
        b4 = Button(win, Point(175,170),120,30,"Remove")
        b4.activate ()
        b5 = Button(win, Point(175,200),120,30,"Search")
        b5.activate ()
        b6 = Button(win, Point(175,240),120,30,"Exit")
        b6.activate ()

        pt = win.getMouse()
        while not b6.clicked(pt):
            if b1.clicked(pt):
                self.addCustomer()   
            if b2.clicked(pt):
                self.addItem()
            if b3.clicked(pt):
                self.addPurchase()
            if b4.clicked(pt):
                self.Remove()
            if b5.clicked(pt):
                self.Search()
            pt = win.getMouse()
        win.close()


#Ask about line 579 , what does it return in the second loop since we dont have any variable "found"
#Answer : after getting the midpoint throughy the loop the first time, in the else part of the loop the first point and last point change
#giving a new midpoint when going through the loop all over again to get the found.
        
#How would I print output in the actual search or remove window. " Would I assign a variable to  "output" from
#sort function or is there like a get output function that can be used to retrieve output

# text = Text(...)
# if output == False
#   text.setText("Could not find")
# else
#   text.setText("Customer Found")
#Search and Remove Item function won't work     
        

        
