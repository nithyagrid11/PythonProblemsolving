def Armstrong_numb():
    digits = []
    n = int(input('How many digits?: '))
    for i in range(n):
        numb = int(input("Enter a digit: "))
        digits.append(numb)
    print(digits)
    numb_of_digits = len(digits)
    for i in range(len(digits)):
        if i < len(digits):
            result = digits[i] ** numb_of_digits
    return result
print(f'Armstrong Number is {Armstrong_numb()}')
#pr practise