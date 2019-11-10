# Write a function copy_string which takes a string and recursively, character
# by character creates a copy of it.


def copy_string(string: str) -> str:
    string_copy = ''
    i = 0
    while i < len(string):
        string_copy += string[i]
        i += 1
    else:
        return string_copy


print(copy_string("Hello, Dave! This is my homework."))
