def RecursiveMin(L):
  if len(L)==2:
     if L[0]<L[1]:
         return L[0]
     else:
        return L[1]
  else:
    X= RecursiveMin(L[1:])
    if L[0]<X:
        return L[0]
    else:
        return X

inp = [int(i) for i in input('Enter Input : ').split()]
print("Min :",RecursiveMin(inp))
