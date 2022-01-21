NumN=0
NumF=0

def max(i,inp):
    global NumN,NumF
    if(i==len(inp)):
        print("Max :",NumF)
    else:
        if i == 0:
            NumF = int(inp[i])
            NumN = int(inp[i])
        else:
            NumN=int(inp[i])
        
        if NumN<=NumF:
            NumF=NumF
        else:
            NumF=NumN
        i+=1

        return max(i,inp)

inp = input('Enter Input : ').split()
max(0,inp)