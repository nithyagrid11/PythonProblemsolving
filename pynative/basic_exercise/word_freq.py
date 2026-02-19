def word_freq(haystack,needle):
    words = haystack.lower().split()
    new_needle = needle.lower()
    freq = 0
    for word in words:
        if word == new_needle:
            freq += 1
    return freq
print(word_freq("Emma is good developer. Emma is a writer and emma also dances",'is'))