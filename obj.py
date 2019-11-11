"""
 Built-in function: 64
  @property , @classmethod 
  
  Built in constants : True, False, None, NotImplemented (__eq__(), __lt__(), __add()__, etc.), Ellipsis, __debug__, quit, exit,copyright, license,credits
  
  
"""
# def enumerate(sequence, start=0):
#     n = start
#     for elem in sequence:
#         yield n, elem
#         n += 1

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons)))
# for i in range(0, 5):
#     print(i, end = " ")

class Animal:
  """ A valid docstring attribute """

  name="Cow"  # an attribute inside the class
  
  def __init__(self):   # default constructor, will be invoked on class instatiation
    self.name = "COW"

  def printName(self):
          print(self.name)

# aObj = Animal() # aObj is local variable
# aObj.printName()

        
# class Animal:

#   def __init__(self):
#     print("Default constructor")

#   def sound(self):
#     print("Sound")

#   def __init__(self, p1):
#         print(p1)

# obj = Animal
# obj.sound("")
# obj1 = Animal(2)