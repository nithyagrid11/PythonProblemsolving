def cum_sum():
    print("Printing current and previous number sum in a range(10)")
    y = 0
    for i in range(10):
        print(f'Current number {i}',end = ' ')
        print(f'Previous number {y}', end = ' ')
        sum = i + y
        print(f'Sum: {sum}')
        y = i
print(cum_sum())