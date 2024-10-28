
print(text[2])
print(text[3])
print(text)
print(text[0:3])
print(text[::2])
print(text[1::2])
print(text[::-1])
print(text[::-2])
str = 'Hello'
print(len(str)) 
str = 'TEST-STR'
print(len(str))

test_strings = ['Hello', 'TEST-STR'] 

for test in test_strings:
    print(f"Обработка строки: '{test}'")
    process_string(test)
    print() 