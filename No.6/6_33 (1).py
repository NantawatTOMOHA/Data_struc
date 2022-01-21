def REC_binary(number, digit):
    if number == 0:
        return print(str(bin(number)).replace('0b', '').zfill(digit))
    return REC_binary(number - 1, digit), print(str(bin(number)).replace('0b', '').zfill(digit))


inp = int(input('Enter Number : '))
if inp >= 0:
    REC_binary((2 ** inp) - 1, inp)
    
else:
    print('Only Positive & Zero Number ! ! ! ')