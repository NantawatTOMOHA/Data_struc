def shell_sort(inp, n):
    h = 4
    while h > 0:
        for i in range(h, len(inp)):
            sh = inp[i]
            j = i
            n += 1
            while j >= h and inp[j - h] > sh:
                n += 1
                inp[j] = inp[j - h]
                j -= h
            inp[j] = sh
        h //= 2
    return n

n= 0

print(" *** Shell sort ***")
inp = [int(n) for n in input("Enter some numbers : ").split()]
l = shell_sort(inp, n)
print()
print(inp)
print("Data comparison = ",l)