# let's create  a project  over stack : 
class Stack: 
    def __init__(self): 
        self.lst=[]
    def push(self,data):
        self.lst.append(data)

class Serach(Stack): 
    def serach(self,iteam): 
        n=  len(self.lst)
        for i in range(0, n ): 
            if self.lst[i]  ==iteam : 
                print('get' )
            else:
                print('not get  ')

s=  Stack()
s.push('tony')
s.push('stack')
print(s.lst)
c=  Serach()
c.serach('tony')
print(c.serach)
