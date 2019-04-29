#implementation using array
#class Stack:
#    def __init__(self):
#        self.items = []

#    def push(self, item):
#        self.items.append(item)

#    def pop(self):
#        return self.items.pop()


#implementation using lists
class Stack:
    def __init__(self):
        self.stack = list()
    
        #insertion -> append item to the stack list
    def push(self, item):
        self.stack.append(item)

        #delete -> pop item on the top of the stack, returns this item
    def pop(self):
        return self.stack.pop()
        
        #return length of stack
    def size(self):
        return len(self.stack)

#initialize stack
s = Stack()

#adding items to the stack
s.push(56)
s.push(45)
s.push(34)

#Checking for size before and after the pop
print(s.size())
print(s.pop())
print(s.size())





