k = 0
def mergeSort(ls):
    global k
    if len(ls) > 1:
        m = len(ls)//2
        L = ls[:m]
        R = ls[m:]
        mergeSort(L)
        mergeSort(R)
        c1, c2, c3 = 0, 0, 0
        while c1 < len(L) and c2 < len(R):
            if L[c1] < R[c2]:
                ls[c3] = L[c1]
                c1 += 1
            else:
                ls[c3] = R[c2]
                c2 += 1
            c3 += 1
            k += 1
        while c1 < len(L):
            ls[c3] = L[c1]
            c1 += 1
            c3 += 1
        while c2 < len(R):
            ls[c3] = R[c2]
            c2 += 1
            c3 += 1

def printAns(inp):
    for i in range(len(inp)):
        print(inp[i], end=" ")

print(' *** Merge sort ***')
inp = [int(n) for n in input('Enter some numbers : ').split(' ')]
mergeSort(inp)
print()
print("Sorted -> ", end='')
printAns(inp)
print()
print('Data comparison = ', k)