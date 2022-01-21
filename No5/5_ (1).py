
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail= None
        self._size = 0

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        cur,st = self.head,str(self.head.value) + ' '
        while cur.next != None:
                st += str(cur.next.value ) + ' '
                cur = cur.next 
        return st

    def isEmpty(self):
        return self.head == None
    
    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.prev != None:
            s += str(cur.prev.value) + " "
            cur = cur.prev
        return s

    def insert(self,sq,value):
        Strlen=self._size
        self._size = self._size + 1
        if(sq<0):
            chck=sq*-1
        else:
            chck=sq
        if(Strlen>=chck):
            if(sq>0):
                if(Strlen>sq):
                    islen=sq-1
                    node=self.head
                    for i in range(islen):
                        node=node.next
                        ISnode=Node(value)
                        Cnode=node.next
                        node.next=ISnode
                        ISnode.next=Cnode
                        ISnode.prev=node
                        Cnode.prev=ISnode
                else:
                    Inputnode=Node(value)
                    Inputnode.prev=self.tail
                    self.tail.next = Inputnode
                    self.tail = Inputnode 
            if(sq<0):
                sq1=(Strlen+sq)-1
                islen1=((Strlen+sq)-1)
                if(Strlen>sq1):
                    node=self.head
                    for i in range(sq1):
                        node=node.next
                    ISnode=Node(value)
                    Cnode=node.next
                    node.next=ISnode
                    ISnode.next=Cnode
                    ISnode.prev=node
                    Cnode.prev=ISnode

                else:
                    Inputnode=Node(value)
                    Inputnode.next=self.head
                    self.head.prev = Inputnode
                    self.head = Inputnode 
            if(sq==0):
                if self.isEmpty():
                    self.head = Node(value)
                    self.tail = self.head
                    return 0
                elif(self.tail is None and self.head is not None):
                    node = self.head
                    self.tail=node
                    self.head = Node(value)
                    self.head.next = node
                    node.prev=self.head
                elif(self.tail is not None and self.head is not None):
                    Anode= self.head
                    self.head = Node(value)
                    Anode.prev=self.head
                    self.head.next=Anode
        else:
            if(sq>0):
                if self.isEmpty():
                    self.head = Node(value)
                    self.tail = self.head
                    return 0
                else:
                    Inputnode=Node(value)
                    cnode999=self.tail
                    Inputnode.prev=self.tail
                    cnode999.next = Inputnode
                    self.tail = Inputnode 
            if(sq<0):
                if self.isEmpty():
                    self.head = Node(value)
                    self.tail = self.head
                    return 0
                else:
                    Inputnode=Node(value)
                    CnodeN999 = self.head
                    Inputnode.next=self.head
                    CnodeN999.prev = Inputnode
                    self.head = Inputnode                

    def append(self,value):
        self._size = self._size + 1
        if self.isEmpty():
            self.head = Node(value)
            return 0
        elif(self.tail is None and self.head is not None):
            node = self.head
            node.next = Node(value)
            self.tail=node.next
            Newnode = node.next
            Newnode.prev = node 
        elif(self.tail is not None and self.head is not None):
            
            Inputnode=Node(value)
            Inputnode.prev=self.tail
            self.tail.next = Inputnode
            self.tail = Inputnode
        
    def addHead(self,value):
        self._size = self._size + 1
        if self.isEmpty():
            self.head = Node(value)
            return 0
        elif(self.tail is None and self.head is not None):
            node = self.head
            self.tail=node
            self.head = Node(value)
            self.head.next = node
            node.prev=self.head
        elif(self.tail is not None and self.head is not None):
            Anode= self.head
            self.head = Node(value)
            Anode.prev=self.head
            self.head.next=Anode
        
            

    def search(self, value):
        node = self.head
        if self.isEmpty():
            return 'Not Found'
        else:
            while node.next != None:
                if node.value == value:
                    return 'Found'
                else:
                    node = node.next
            if node.value == value:
                return 'Found'
        return 'Not Found'

    def index(self, value):
        index = 0
        node = self.head
        if self.isEmpty():
            return -1

        if self.size() == 1:
            if node.value == value:
                return index
        
        while node.next != None:
            if node.value == value:
                return index
            else:
                node = node.next
                index = index + 1
        if node.value == value:
            return index
        else:
            return -1

    def size(self):
        return self._size

    def pop(self,pos):
        index = 0
        if pos >= self.size() or pos < 0:
            return 'Out of Range'

        if pos == 0 and self.size() == 1:
            self.head = None
        elif pos == 0:
            self.head = None
            self.head = self.head.next
        else:
            node = self.head
            while index != pos -1:
                index = index + 1
            else:
                node.next = node.next.next

        self._size = self._size - 1
        return 'Success'  
    

        

if __name__ == "__main__":
    L = LinkedList()
    inp = input('Enter Input : ').split(',')
    for i in inp:
        if i[:2] == "AP":
            L.append(i[3:])
        elif i[:2] == "AH":
            L.addHead(i[3:])
        elif i[:2] == "SE":
            print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
        elif i[:2] == "SI":
            print("Linked List size = {0} : {1}".format(L.size(), L))
        elif i[:2] == "ID":
            print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
        elif i[:2] == "PO":
            before = "{}".format(L)
            k = L.pop(int(i[3:]))
            print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
        elif i[:2] == "IS":
            data = i[3:].split()
            L.insert(int(data[0]), data[1])
    print("Linked List :",L)
    print("Linked List Reverse :", L.reverse())