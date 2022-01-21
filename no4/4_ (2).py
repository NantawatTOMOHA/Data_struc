class Queue:
    def __init__(self):
        self.item = []

    def push(self,item):
        self.item.append(item)

    def deQueue(self):
        if self.size() > 0:
            return self.item.pop(0)
        else:
            print('Empty')

    def size(self):
        return len(self.item)

    def __str__(self):
        if self.size() > 0:
            return ', '.join(str(item) for item in self.item)
        else:
            return 'Empty'

    def isEmpty(self):
        return len(self.item) == 0

Inp = input('Enter Input : ').split(',')
Q = Queue()
DQ = Queue()
A = Queue()


for i in Inp:
    i = i.split()
    if i[0] == 'E':
        Q.push(str(i[1]))
        ls=len(Q.item)-1
        print("Add",str(i[1]),'index is',ls)    
    elif i[0] == 'D':
        if Q.isEmpty():
            print('-1')
        else:
            Num = Q.deQueue()
            ls1=len(Q.item)
            print('Pop',Num,'size in queue is',ls1)
            

if(len(Q.item)==0):
    print('Empty')
else:
        
        print('Number in Queue is : ',str([x for x in Q.item]) )