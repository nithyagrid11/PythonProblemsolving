def Palindrome(n):
    i,j=0, len(n)-1
    while i<j:
        if n[i]!=n[j]:
            return 'Not Palindrome'
        i+=1
        j-=1
    return 'Palindrome'
print(Palindrome('sos'))
print(Palindrome('level'))
print(Palindrome('Hai'))