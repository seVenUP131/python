def count_words(s):
    words = s.split()
    return len(words)

test_strings = [ 
    'Hello world',
    'a b c',
    'test',
    'test1 test2 test3 test4 test5'
]

for test in test_strings:
    print(f"количество слов в строке '{test}': {count_words(test)}")