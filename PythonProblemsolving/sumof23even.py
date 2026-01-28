def Sum_of_first_23_even(n):
    sum=0
    even_first=2
    for i in range(n):
        sum += even_first
        even_first += 2
    return sum
print(Sum_of_first_23_even(23))