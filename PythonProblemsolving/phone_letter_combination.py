def combination():
    data = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    digits = input('Enter digits: ')
    result = ['']
    for digit in digits:
        if digit not in data:
            return 'Invalid digit'
        letters = data[digit]
        new = []
        for prefix in result:
            for letter in letters:
                new.append(prefix + letter)
        result = new
    return result

print(combination())