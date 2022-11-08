class Stack :
    def __init__(self): 
        self.lst=[]
    
    def isEmpty(self): 
        return self.lst == [ ]
    def push(self,data): 
        self.lst.append(data)
    def pop(self):
        return  self.lst.pop()
    def peak(self): 
        return self.lst[-1]
    def size(self): 
        return len(self.lst)
if __name__ == '__main__':
    s=Stack()
    s.push('j')
    s.push('k')
    s.push('k')
    print(s.lst) 
    