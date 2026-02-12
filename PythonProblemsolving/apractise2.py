'''def unique_word(s):
    freq={}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
print(unique_word('nithya'))'''

'''math = {"a": 80, "b": 90}
science = {"b": 70, "c": 85}
result = {}
for student,score in math.items():
    if student not in result:
        result[student] = {}
    result[student]['math'] = score
for student,score in science.items():
    if student not in result:
        result[student] = {}
    result[student]['science'] = score
print(result)'''

'''def group_numb(n):
    group = {'even': [], "odd": []}
    for num in n:
        if num % 2 == 0:
            group['even'].append(num)
        else:
            group['odd'].append(num)
    return group
print(group_numb([1,2,3,4,5,6,7,8,9,10,11]))'''

'''def custom_range(start,end):
    for num in range(start,end):
        if num % 3!=0:
            yield num ** 2
for value in custom_range(1,10):
    print(value)'''


'''def log_read(logs):
    for i in logs:
        if i.startswith("ERROR"):
            yield i
logs = [
    "INFO: start",
    "ERROR: failed login",
    "WARNING: retry",
    "ERROR: crash"
]
for n in log_read(logs):
    print(n)'''

#input: [1,[2,3],[4,[5]] ]
#        0   1      2
#output: 1,2,3,4,5
'''def nested_list(list1):
    for num in list1:
        if isinstance(num,list):        #isinstance(object,type)
            yield from nested_list(num)
        else:
            yield num
data = [1,[2,3],[4,[5]] ]
for x in nested_list(data):
    print(x)'''

#generator + list
'''def even_num(lst):
    for num in lst:
        if num % 2 == 0:
            yield num
data = [1,2,3,4,5,6,7,8,9,10,12,11,14]
for x in even_num(data):
    print(x)'''

#generator + set
'''def unique_char(s):
    seen = set()
    for ch in s:
        if ch not in seen:
            yield ch
            seen.add(ch)
data = 'banana'
for x in unique_char(data):
    print(x)'''

#generator + dict
'''def word_length(s):
    s1 = s.split()
    for word in s1:
        if len(word) > 3:
           yield (word,len(word))
data = 'Today is Tuesday, 10th Feb 2026'
for x in word_length(data):
    print(x)'''

#generator + int
#i/p: [1,2,3] o/p:1,3,6
'''def cum_sum(n):
    sum = 0
    for i in n:
        if isinstance(i,int):
            sum += 1
            yield sum
data = [1,2,3]
for x in cum_sum(data):
    print(x)'''

#generator + dict - level2
#[a,b,a,a] -> (a,1), (b,1), (a,2), (a,3)
'''def current_count(list1):
    dict1 = dict()
    for item in list1:
        if item in dict1:
            dict1[item] += 1
        else:
            dict1[item] = 1
        yield (item,dict1[item])
data = ['a','b','a','a']
for x in current_count(data):
    print(x)'''

#generator + set - level2
#Yield an element only when it appears for the first time.
'''def first_time_seen(list1):
    seen = set()
    for i in list1:
        if i not in seen:
            seen.add(i)
            yield i
data = ['a','a','b','c','c','b','d']
for x in first_time_seen(data):
    print(x)'''

#generator + dict - level2
#i/p: [1,2,3,4,5]
# o/p: {'odd':[1]}
#      {'odd':[1], 'even':[2]}
#      {'odd':[1,3], 'even':[2]}
'''def intermediate_grouping(list1):
    dict1 = {'odd': [], 'even': []}
    for i in list1:
        if i % 2 != 0:
           dict1['odd'].append(i)
        else:
            dict1['even'].append(i)
        yield dict1.copy()
data = [1,2,3,4,5]
for x in intermediate_grouping(data):
    print(x)'''

#generator + list - level3
'''def flatten(list1):
    for i in list1:
        if isinstance(i,list):
            yield from flatten(i)
        else:
            if i % 2 == 0:
                yield i
data = [1,[1,2],[3,4],[3,[5,6]]]
for x in flatten(data):
    print(x)'''

#generator + dict - level3
#{"a":1,"b":{"c":2,"d":3}} → 1,2,3
'''def flatten_dict(dict1):
    for key,value in dict1.items():
        if isinstance(value,dict):
            yield from flatten_dict(value)
        else:
            yield value
data = {"a":1,"b":{"c":2,"d":3}}
for x in flatten_dict(data):
    print(x)'''

#generator + collections
#data = {"a": 1,
#        "b": [2, {"c": 3, "d": [4, 5] } ],
#        "e": {"f": 6} }
'''def flatten_values(dict1):
    if isinstance(dict1,dict):
        for value in dict1.values():
            yield from flatten_values(value)
    elif isinstance(dict1,list):
        for item in dict1:
            yield from flatten_values(item)
    else:
        yield dict1
data = {
    "a": 1,
    "b": [2, {"c": 3, "d": [4, 5]}],
    "e": {"f": 6}
}
for x in flatten_values(data):
    print(x)'''

def expense_func(id,description,amount):
        Day = dict()
        while True:
           Day['id'] = id
           Day['desc'] = description
           Day['amount'] = amount
print(expense_func(1,'coffee',50))
