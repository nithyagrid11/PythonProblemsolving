def anagram(str1,str2):
    if len(str1) != len(str2):
        print('Give same length words')
        return
    s1 = sorted(str1)
    s2 = sorted(str2)
    d1 = dict()
    d2 = dict()
    for ch1 in s1:
        d1[ch1] = d1.get(ch1, 0) + 1
    print(d1)
    for ch2 in s2:
        d2[ch2] = d2.get(ch2, 0) + 1
    print(d2)

    return d1 == d2
    '''if d1.keys() == d2.keys(): #done with checking if each char in str1 is in str2 
        for ch in d1:
            if d1[ch] == d2[ch]:
                return True
    else:
        return False''' #not necessary of if statement as python dictionary does that internally

print(anagram('cinema','iceman'))

'''char1 = list()
    for ch in str1:
        char1.append(ch)
    char1.sort()
    print('Characters in str1 are: ',char1)
    char2 = list()
    for ch in str2:
        char2.append(ch)
    char2.sort()
    print('Characters in str2 are: ',char2)
    for ch1 in char1:
        for ch2 in char2:
            if ch1 is ch2:
                return True
            else:
                return False'''