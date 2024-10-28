def is_palindrome(s):
    return s == s[::-1]


strings = ['abcсba', 'level', 'racecar']

palindromes = list(filter(is_palindrome, strings))

print(palindromes)