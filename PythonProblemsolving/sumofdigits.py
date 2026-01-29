def sum_of_digits(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
n = int(input('Enter a number: '))
print(f'Sum of {n} digits is {sum_of_digits(n)}')