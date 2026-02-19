def vowel_freq(s):
    vowels = ['a','e','i','o','u']
    count = 0
    '''for i in range(len(s)):
        if s[i] in vowels:
            count += 1
    return count'''
    for i in s.lower():
        if i in vowels:
            count += 1
    return count
print(vowel_freq("Learning Python is fun!"))