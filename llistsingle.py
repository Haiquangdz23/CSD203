


from ast import Delete


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
  
    # 1 & 2: Allocate the Node &
    #        Put in the data
        newNode = Node(data)
          
    # 3. Make next of new Node as head
        newNode.next = self.head
          
    # 4. Move the head to point to new Node 
        self.head = newNode
    


    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode
        newNode.next = None


    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next 
            

    def prepend(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

    def addtoafter(self, key, data):
        if not key:
            print("Previous is not in the list")
            return
        newNode = Node(data)
        newNode.next = key.next
        key.next = newNode
    
    def Deletion(self, key):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur.next = None
            return
 

llist = linkedList()
llist.append("A")
llist.append("B")
llist.append("BC")
llist.prepend("AD")
llist.addtoafter(llist.head.next, "Hai")
llist.Deletion("A")
llist.push('HAi')


llist.print_list()
