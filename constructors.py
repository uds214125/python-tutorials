#--------------------------------- two way to pass the data to the class attribute
#1. by constructor

# class Animal:
#     name=""

#     def __init__(self, name):
#           self.name = name
#     def printName(self):
#         print(self.name)

# obj = Animal("cow")
# obj.printName()

#1. by gettter-setter 

class Animal:

    def __init__(self, name):
          self.name=""

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    # def printName(self):
    #     print(self.name)

obj = Animal("")
obj.setName("cow")
name = obj.getName()
print("Animal name : ", name)