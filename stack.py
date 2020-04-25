
class Stack:
    array=[]
    index=-1
    def __init__(self):
        self.array=[]
        self.index=0
    def push(self,ele):
        self.array.append(ele)
        self.index+=1
    def pop(self):
        if self.index==-1:
            return -1
        self.index-=1
        return self.array[self.index+1]
    def peek(self):
        return self.array[self.index]

