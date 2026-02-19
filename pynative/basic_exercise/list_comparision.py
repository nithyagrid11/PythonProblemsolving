def comparision(list1):
    first = list1[0]
    last = list1[-1]
    if first == last:
        return True
    else:
        return False
print(comparision([10,20,30,40,10]))
print(comparision([75,65,35,75,30]))