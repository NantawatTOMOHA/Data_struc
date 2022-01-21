data = [int(x) for x in input('Enter number end with (-1) : ').split()]

Data = [0]* (max(data)+1)
Storage = []

if -1 not in data:
    print('Invalid INPUT !!!')
else:
    for i in data:
        if i!=-1:
            Data[i]+=1
            Storage.append(i)
        else:
            break
    found = 0
    for i in Storage:
        if Data[i]>len(Storage)/2:
            print(i)
            found = 1
            break
    if found==0:
        print('Not found')