def frequency(n):
    freq = {}
    for i in n:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
print(frequency([1,1,1,2,2,3,4,5,1,2,3,3]))