def first_duplicate(lst):
    seen = []
    for r in range(0,len(lst)):
        if lst[r] in seen:
            return lst[r]
        else:
            seen.append(lst[r])
print(first_duplicate([1,2,2,3,1,2]))