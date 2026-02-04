#2-pointer approach
def Longest_palindrome(s):
    max_str = s[0:1]
    def expand_from_center(l,r):
        while l>=0 and r<len(s) and s[l] == s[r]: #we are checking only if it is palindrome so no need to call the is_Palindrome func
            l-=1
            r+=1
        return s[l+1:r]
    i = 0
    for i in range(len(s)):
        odd = expand_from_center(i,i)
        even = expand_from_center(i,i+1)
        if len(odd) > len(max_str):
            max_str = odd
        if len(even) > len(max_str):
            max_str = even
    return max_str
print('Largest Palindrome: ', Longest_palindrome('aacbbcdd'))
print('Largest Palindrome: ', Longest_palindrome('avcccdddccwqzszsam'))


#brute-force method
'''def is_Palindrome(n):
    i,j=0, len(n)-1
    while i<j:
        if n[i]!=n[j]:
            return False
        i+=1
        j-=1
    return True
def Longest_Palindrome(s):
    i=0
    j=1
    longest_palindrome=""
    for i in range(len(s)):
        for j in range(i,len(s)):
            substring = s[i:j+1] #extract substring starting at i and ending at j
            if is_Palindrome(substring) and len(substring) >= len(longest_palindrome):
                longest_palindrome = substring
    return longest_palindrome
print(Longest_Palindrome('aacbbcdd'))'''

