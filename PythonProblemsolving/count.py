'''def count_num(n):
    dict1 = {}
    for i in n:
        if i not in dict1:
            dict1[i] = 0
        dict1[i] += 1
    return dict1
print(count_num(['a','a',1,2,3,2,3,4,2,5,4,3,1]))'''

'''from collections import Counter
my_list = [1,1,2,3,2,3,2,1,3,2,4,5,4]
print(Counter(my_list))'''

'''from datetime import date
d = date(2005,1,11) #date(year,month,date)
print(d)'''

import math
value = 5.2
print(math.floor(value))
print(math.ceil(value))