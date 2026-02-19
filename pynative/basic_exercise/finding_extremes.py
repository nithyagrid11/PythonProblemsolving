def finding_extremes(list1):
    largest = list1[0]
    smallest = list1[0]
    for num in list1:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    print('Largest: ',largest, "Smallest: ",smallest)
finding_extremes([45,2,89,12,7])

#using min() and max()
list2 = [45,2,56,4,76,1]
longest = max(list2)
smallest = min(list2)
print(f'Largest: {longest}')
print(f'Samallest: {smallest}')