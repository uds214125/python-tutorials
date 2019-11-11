# default argument
class Square:

    def __init__(self):
        self.result =0
    def sqrt(self,number=1):
        return number*number

    def anySqrt(self, *args):
        for i in len(args):
            self.result = i*i
        return self.result

t1 = Square()
print(t1.sqrt(2))
print(t1.sqrt()) # default number will be used

print(t1.anySqrt(1,2,3))
# any no. of arguments


# any no. keyword arguments

