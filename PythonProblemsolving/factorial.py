def Factorial(n):
    if n<0:
        return 'Not applicable'
    num = 1
    for i in range(1,n+1):
        num *= i
    return num
n = int(input("Enter a number: "))
print(f'Factorial of {n} is {Factorial(n)}')