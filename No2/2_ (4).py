def mod_position(arr, s):
    temp = 1
    while(temp <= len(arr)):
        if temp%s == 0:
            ans.append(arr[temp-1])
        temp+=1
    return print(ans)



arr,s= input("*** Mod Position ***\n"+"Enter Input : ").split(",",2)
s=int(s)
ans=[]
mod_position(arr, s)
