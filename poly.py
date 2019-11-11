class Animal:

    def __init__(self,name="Default"):
        self.name =name

obj = Animal()
# print(obj.name)
obj1 = Animal("hola")
# print(obj1.name)

# one way to acheive ploymorphism
class City:
    def __init__(self, city=None):
        self.city = city

    def __repr__(self):
        # return self.city if self.city else ""
        return (lambda:"", lambda:self.city)[self.city!= None]() # operands are lazily evaluated

c1=City()
print(c1)
c1=City("BLR")
print(c1)

# buit-in function which demonstrate example of polymorphism nature
# len("string") or, len({"name":"A","roll":122}) or len([1,2,33,4])

# Can multiple function will have the same name in Python ?  No

