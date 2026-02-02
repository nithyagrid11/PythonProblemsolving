def sieve(n):
    prime =[True] * (n+1)

    prime[0] = False
    prime[1] = False

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p*p,n+1,p):
                prime[i] = False
        p+=1

    res=[]
    for i in range(2,n+1):
        if prime[i] == True:
            res.append(i)
    return res
print(f'All primes upto {15} are {sieve(15)}')