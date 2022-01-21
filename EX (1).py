def bi_search(l, R, array, x):
    if l > R:
        return "Not found"
    mid = (l+R)//2
    if array[mid] == x:
        return "Found"
    if array[mid] > x :
        return bi_search(l,mid-1,array,x)
    else:
        return bi_search(mid+1,R,array,x)

inp = input('Enter Input : ').split('/')
arr, n = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), n))