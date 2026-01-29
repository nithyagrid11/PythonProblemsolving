def Reverse_a_String(s):
    lst = list(s)
    i = 0
    j = len(lst)-1

    while i<j:
        lst[i] , lst[j] = lst[j], lst[i]
        i+=1
        j-=1
    return lst
    
s = input('Enter a string: ')
print(f'Reverse of "{s}" is {Reverse_a_String(s)}')
