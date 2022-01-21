count=0
countN=0
def ShitString(inp):
    global count,countN
    if inp == '':
        print()
        return 0
    if count ==0:
        print(inp[0],end='*')
        count+=1
        countN+=1
    else:
        print(inp[0],end='~')
        count-=1
        countN+=1
    return ShitString(inp[1:])

inp=input("Enter Input : ")
ShitString(inp)
print(countN)
