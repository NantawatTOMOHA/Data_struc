Data = int(input('Enter a positive number : '))
if Data < 1:
    print(str(Data)+" is too low.")
elif Data < 16 :
    print(' '.join(["%X"%(i) for i in range(1,Data+1) ]))
    for i in range(2,Data):
        print("%X"%(i) + ((Data*2)-3)*' ' + "%X"%(i-1))
    print("%X "%(Data) + ' '.join(["%X"%(i) for i in range(1,Data) ]))
elif Data >= 16:
    print(str(Data)+" is too high.")
