n = int(input('Input : '))
if n>0:
    for i in range(n):
        print(i*'*'+(n*2-i*2)*' '+i*'*')
    for i in range(n,0,-1):
        print(i*'*'+(n*2-i*2)*' '+i*'*')
else:
    print('!!!Please enter number greater than zero!!!')