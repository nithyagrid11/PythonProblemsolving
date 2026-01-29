def is_Palindrome(n):
    list1 = list(n)
    i,j=0, len(list1)-1
    while i<j:
        if list1[i] != list1[j]:
            return False
        i+=1
        j-=1
    return True
def MaxPalindrome(s):
    i=0
    j=1
    longest=""
    for i in range(len(s)):
        for j in range(i,len(s)):
            substring = s[i:j+1] #extract substring starting at i and ending at j
            if is_Palindrome(substring) and len(substring) >= len(longest):
                longest = substring
    return longest
#print('Largest Palindrome: ', MaxPalindrome('aabcbcdd'))
#print(Palindrome('sos'))
#print(Palindrome('hai'))
#print(MaxPalindrome('aabcbcdd'))
#abccdd
print(MaxPalindrome('avcccdddccwqzszsam'))