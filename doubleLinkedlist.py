class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
class doublyLinkedList:
    def __init__(self):
        self.head = None
    # c1   
    def addToHead(self, newElement):
        newNode = Node(newElement)
        if(self.head == None):
          self.head = newNode
          return
        else:
          self.head.prev = newNode
          newNode.next = self.head
          self.head = newNode        

    # c2
    def addToTail(self, newElement):
        newNode = Node(newElement)
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
    
    # c3       
    def addAfter(self, newElement, position):
        newNode = Node(newElement)
        if(position < 1):
            print("\n location >= 1.")
        elif (position == 1):
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:    
            temp = self.head
            for i in range(1, position-1):
                if(temp != None):
                    temp = temp.next   
            if(temp != None):
                newNode.next = temp.next
                newNode.prev = temp
                temp.next = newNode  
                if (newNode.next != None):
                    newNode.next.prev = newNode
    
    # c4            
    def deleteFromHead(self):
        if(self.head != None):
            
            temp = self.head

            self.head = self.head.next 
    
            temp = None 

        if(self.head != None):
            self.head.prev = None
    
    # c5
    def deleteFromTail(self):
        if(self.head != None):
            if(self.head.next == None):
                self.head = None
            else:
                temp = self.head
                while(temp.next.next != None):
                    temp = temp.next
                
                lastNode = temp.next
                temp.next = None
                lastNode = None
                
   
    # c7
    def count(self):
        temp = self.head
        i = 0
        while (temp != None):
            i +=1
            temp = temp.next
        return i
  
            
  
        
        

s = doublyLinkedList()
s.addToHead(1)
s.addToHead(6)
s.addToTail(20)
s.addAfter(100,1)

s.deleteFromHead()
s.deleteFromTail()


print("Number of nodes : ", s.count())

