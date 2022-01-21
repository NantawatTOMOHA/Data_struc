class MyInt:
    def __init__(self,x):
        self.num = int(x)
    
    def isPrime(self):
        count = 0
        if self.num < 2:
            return False
        for i in range(2,int(self.num/2)):
            if self.num%i == 0:
                count+=1
        return count==0
    
    def showPrime(self):
        sequnce = []
        storage = [0]*(self.num+1)
        if self.num < 2:
            return "!!!A prime number is a natural number greater than 1"
        for i in range(2,self.num+1):
            if storage[i] == 0:
                SS = 2
                count = i
                while count < self.num:
                    count = i*SS
                    SS+=1
                    if count < len(storage):
                        storage[count] = 1
        for i in range(2,len(storage)):
            if storage[i] == 0:
                sequnce.append(str(i))
        return " ".join(sequnce)

    def __sub__(self,other):
        return self.num - int(other.num/2)

print(" *** class MyInt ***")
Data = [int(e) for e in input("Enter 2 number : ").split()]
a = MyInt(Data[0])
b = MyInt(Data[1])
print(a.num,"isPrime :",b.isPrime())
print(b.num,"isPrime :",b.isPrime())
print("Prime number between 2 and",a.num,":",a.showPrime())
print("Prime number between 2 and",b.num,":",b.showPrime())
print(a.num,"-",b.num,'=',a-b)