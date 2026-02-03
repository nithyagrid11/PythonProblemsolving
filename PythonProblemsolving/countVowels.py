def Count_Vowels(s):
    vowels = ['a','e','i','o','u']
    count = 0
    for i in range(0,len(s)):
        if s[i] in vowels:
            count += 1
    return count
print(Count_Vowels('aeiousdfu'))
