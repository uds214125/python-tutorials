
class Stack:
  st = []
  max = 5
  
  def __init__(self):
      pass
  
  def push(self,el):
      if len(self.st)>max:
          return "Full"
      else:
         self.st.append(el)
         
  def disp(self):
      return self.st 
       
       
ob = Stack()
ob.push(2)

print(ob.disp())
# for i in len(ob.disp()):
    # print(i,end="->")