def Fib(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        next_num = a + b
        a = b
        b = next_num
Fib(10)