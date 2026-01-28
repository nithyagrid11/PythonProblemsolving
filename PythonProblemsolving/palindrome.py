def Palindrome(n):
    list1 = list(n)
    i,j=0, len(list1)-1
    while i<j:
        if list1[i]!=list1[j]:
            return 'Not Palindrome'
        i+=1
        j-=1
    return 'Palindrome'
print(Palindrome('sos'))
print(Palindrome('level'))
print(Palindrome('Hai'))