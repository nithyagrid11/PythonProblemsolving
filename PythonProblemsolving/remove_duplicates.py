'''def longest_substring(s):
    hash_set = set()
    for i in range(len(s)):
        if s[i] not in hash_set:
            hash_set.add(s[i])
            i += 1
    return hash_set
print(longest_substring('aaeyfghbbg'))'''

'''def longest_substring(s):
    substring = ''
    for i in range(len(s)):
        if s[i] not in substring:
            substring += s[i]
    return substring
print(longest_substring('abccefghbca'))'''

def longest_substring(s):
    seen = set()
    l = 0
    substring_longest = ""
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        if r - l + 1 >len(substring_longest):
            substring_longest = s[l:r+1]
    return substring_longest
print(longest_substring('abccefghbb'))

