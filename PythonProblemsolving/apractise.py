#1
'''a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print(a + b)
print(a * b)
print((a+b)/2)'''

#3
'''def number_check(a):
    if a < 0:
        return 'Negative'
    elif a == 0:
        return 'Zero'
    else:
        return 'Positive'
print(number_check(-1))'''
    
#2
'''def Swap(a,b):
    print(a,b)
    a,b = b,a
    return a,b
Swap(4,5)'''

#4
'''seconds = 30
minutes = (60 * seconds)
hours = (60 * minutes)
print(minutes)
print(hours)'''

#String1
'''def reverse(a):
    if len(a) <= 1:
        return a
    return reverse(a[1:]) + a[0] #recursion
print(reverse('nithya'))'''

#String2
'''def count(s):
    vowels = ['a','e','i','o','u']
    v = 0
    c = 0
    for i in range(0,len(s)):
        if s[i] in vowels:
            v += 1
        else:
            c += 1
    return v,c
print(count('nithya'))'''

#string3
'''def palindrome(a):
    i = 0
    j = len(a) - 1
    while i >=0 and j <len(a):
        if a[i] != a[j]:
            return False
        i+=1
        j+=1
    return True
print(palindrome('abccba'))
print(palindrome('nithya'))'''

#string4
'''def frequency(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq
print(frequency('nithyaaa'))'''

#string5
'''def remove_duplicates(s):
    set1 = set()
    result = ""
    for i in s:
        if i not in set1:
            result += i
            set1.add(i)
    return result
print(remove_duplicates('nniithyaa'))'''

#
'''def duplicates(b):
    seen = set()
    result = []
    for i in b:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result
print(duplicates([1,2,3,3,4,5,1,2,4]))'''

#
'''data = [(1,2), (3,4), (5,6)]
res = []
for a,b in data:
    res.append(a+b)
print(res)'''

#
'''lst = [1,2,1,3,4,2,5,4,2]
lst1 = list(set(lst))
print(lst1)'''

#
'''t = ("apple","banana","apple","orange")
freq = {}
for i in t:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)'''

#
'''a = [1,2,3,4]
b = [3,4,5,6]
common = set(a) & set(b)
unique = set(a) ^ set(b)
print(common)
print(unique)'''

#
'''students = [("Ram",80),("Sita",90),("Hari",70)]
freq = {}
for name,marks in students:
    freq[name] = marks
print(freq)'''

#
'''d = {"a":[1,2,3], "b":[4,5]}
res = []
for num in d.values():
    res.extend(num)
print(res)'''

#
'''t1 = (1,2,3,4)
t2 = (3,4,5,6)

set1 = set(t1)
set2 = set(t2)
common = set1 & set2
union = set1 ^ set2
print(common)
print(union)'''

#
'''data = [
    ("Ram",[80,90]),
    ("Sita",[70,60])
]
freq = {}
for name,marks in data:
    freq[name] = (marks[0] + marks[1])/2
print(freq)'''


