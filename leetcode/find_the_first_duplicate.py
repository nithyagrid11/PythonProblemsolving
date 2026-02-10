def first_duplicate(lst):
    seen = []
    for r in range(0,len(lst)):
        if lst[r] in seen:
            return r
        else:
            seen.append(r)
print(first_duplicate([1,2,3,1,2]))