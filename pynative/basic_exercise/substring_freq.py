#overlapping
def substring_freq(text,substring):
    count = 0
    for i in range(len(text) - len(substring) + 1):
        if text[i:i+3] == substring:
            count += 1
    return count
print(substring_freq('bananaaa','ana'))

#non-overlapping
def substring_freq1(text,substring):
    count = 0
    i = 0
    while i <= range(len(text) - len(substring)):
        if text[i:i+3] == substring:
           count += 1
           i += len(substring)
        else:
            i += 1
    return count
print(substring_freq('bananaaa','ana'))