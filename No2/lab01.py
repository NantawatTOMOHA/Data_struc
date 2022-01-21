def Rshift(num,shift):
     x=0
     x=num >> shift
     return  x

n,s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n),int(s)))