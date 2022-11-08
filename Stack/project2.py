# create a Stack Which avoid the sing simbol  : 
class Stack: 
    def __init__(self):
        self.lst=[]
    def push(self,data):
        token= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  , '1234567890'
        if data in token : 
            self.lst.append(data)
        else:
            print('None:')
if __name__ == '__main__  ' : 
        
    s= Stack()
    s.push('A')
    s.push('-')
    s.push('B')
    s.push('1')
    print(s.lst)
