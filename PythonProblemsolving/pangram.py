def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())
print(is_pangram('Hello, This is Nithya'))
print(is_pangram('The quick brown fox jumps over the lazy dog'))