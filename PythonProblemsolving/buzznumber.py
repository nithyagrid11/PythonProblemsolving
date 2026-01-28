def Buzznum(n):
    if n % 7 ==0 or n % 10 == 7:
        return 'Is a Buzz number'
    else:
        return 'Is not a buzz number'
print(Buzznum(7))
print(Buzznum(14))
print(Buzznum(27))
print(Buzznum(32))
print(Buzznum(2))