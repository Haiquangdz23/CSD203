
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if self.items == None:
            return True
        else:
            return False
       
    def clear(self):
        if self.items is not None:
            return self.items.clear()
        else:
            print("Stack is empty")

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return print("first element of the stack", self.items[len(self.items)-1])
  
    def traverse(self):
        for i in self.items:
            print(i)

s = Stack()
s.push(23)
s.push(22)
s.push(30)
s.top()












