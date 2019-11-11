# This order is also called Linearization of a class and set of rules are called MRO(Method Resolution Order)

class Animal:
    def __init__(self):
        self.name = "Default"
        self.food = "Any"
    def canEat(self):
        print(" {} can eat {} ".format(self.name,self.food))

a1 = Animal()
a1.name = "Cow"
a1.food = "Grass"
a1.canEat()