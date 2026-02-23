def pattern_generation(rows):
    for i in range(rows+1):
        for j in range(i):
            print(i,end=' ')
        print("")
pattern_generation(5)