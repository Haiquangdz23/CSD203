class deque:
    def __init__(self, data):
        self.items = data
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
        
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()
        print('')

    def first(self):
        return self.items[len(self.items)-1]

    def traverse(self):
        for i in self.items:            
            print(i)
    





