# Write a function first_letter which takes a string and returns first
# uppercase letter in it


def first_letter(string: str) -> str:
    i = 0
    while i < len(string) and string[i].islower():
        i += 1
    else:
        return string[i]


print(first_letter("proPerty"))
