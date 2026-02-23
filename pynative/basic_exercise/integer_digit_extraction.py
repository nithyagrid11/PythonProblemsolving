def integer_extraction_reversal(num):
    while num > 0:
        digit = num % 10
        print(digit, end = " ")
        num = num // 10
    print("")
integer_extraction_reversal(7536)