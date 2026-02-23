#converting into string
'''def number_palindrome(num):
    str1 = str(num)
    reverse = str1[::-1]
    if reverse == str1:
        return True
    else:
        return False
print(number_palindrome(123))'''

#using modulous and division
def num_palindrome(n):
    reverse = 0
    original = n
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    return original == reverse
print(num_palindrome(123))
# num % 10 -> we get last digit
#num // 10 -> removes last digit in the original number
# to shift the place of num so we can add next num to right, we multiply with 10
