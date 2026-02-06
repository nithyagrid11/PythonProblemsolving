def isPrime(n):
    if n<=1:
        return 'Not Prime'
    for i in range(2,n):
        if n%i == 0:
            return 'Not Prime'
    return 'Prime'
print(isPrime(4))
print(isPrime(2))
print(isPrime(5))
print(isPrime(1))
print(isPrime(-1))