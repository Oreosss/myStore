#button.py

#Button class for widget


from graphics import *
"""A button is a labelled rectangle in a window . It is activated ordeactivated with the activate() and deactivate() methods.
  The clicked (p)method returns true if the button is active and p is inside it."""

class Button:

    def __init__(self, win, center, width, height, label):
         """Creates a rectangular button
            qb = Button (myWin), Point (0,0) , 20,10, "Quit")"""


         w, h = width/2.0 , height/2.0
         x,y = center.getX(), center.getY()

         self.xmax, self.xmin = x+w , x-w
         self.ymax, self.ymin = y+h , y-h


         p1 = Point (self.xmin, self.ymin)
         p2 = Point (self.xmax, self.ymax)

         self.rect = Rectangle (p1, p2)
         self.rect.setFill ("lightblue")
         self.rect.draw(win)
         self.label= Text (center,label)
         self.label.draw(win)
         self.deactivate()


    def activate(self):
        "Sets this button to activate state"
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active=1
    def deactivate (self):
         "Sets this button to deactivate state"
         self.label.setFill("darkgrey")
         self.rect.setWidth(1)
         self.active=0


    def getLabel (self):
        "Return the label string"
        return self.label.getText()
    def clicked (self,pt ):
        "Return true if button active and p is inside the button"
        return self.active and self.xmin <= pt.getX() <= self.xmax and self.ymin <= pt.getY() <= self.ymax
