'''def second_largest_sum():
    list1 = list()
    n = int(input('Enter the range of list: '))
    for _ in range(n):# O(n)
        number = int(input('Enter a number: '))
        list1.append(number)
    print('Original list:', list1)
    list1.sort() #(n logn)
    print('Sorted list',list1)
    num_3 = list1[-3] #O(1)
    max_num = max(list1) #O(n)
    print(f'Second largest sum: {num_3 + max_num}')
second_largest_sum()
#O(n logn)'''

#consequent 2nd largest sum
'''def consequent_sum():
    numb_list = list()
    n = int(input('Enter the range of list: '))
    if n<3:
        print("Need atleast 3 numbers")
        return
    for _ in range(n):
        number = int(input('Enter the value: '))
        numb_list.append(number)
    print("List: ", numb_list)
    sums = []
    for i in range(n-1):
        pair_sum = numb_list[i] + numb_list[i+1]
        sums.append(pair_sum)
    print("All consequent sums are: ",sums)
    sums.sort()
    print(f'2nd largest consequent sum is {sums[-2]}')
consequent_sum()'''

#optimised consequent 2nd largest
def consequent_optimised():
    numb_list = list()
    n = int(input('Enter the range of list: '))
    if n<3:
        print("Need atleast 3 numbers")
        return
    for _ in range(n):
        number = int(input('Enter the value: '))
        numb_list.append(number)
    print("List: ", numb_list)

    largest = float('-inf')
    second_largest = float('-inf')
    for i in range(n-1):
        pair_sum = numb_list[i] + numb_list[i+1]
        if pair_sum > largest:
            second_largest = largest
            largest = pair_sum
        elif pair_sum > second_largest and pair_sum != largest:
            second_largest = pair_sum
    print("2nd highest sum of consequent numbers is: ",second_largest)
consequent_optimised()