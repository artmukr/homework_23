# Write a function is_palindrome which takes a string and returns boolean
# whether the string is a palindrome or not


def is_palindrome(word: str) -> bool:
    reversed = ''
    i = 0
    while i <= len(word)-1:
        i += 1
        reversed += word[-i]
    else:
        return word == reversed


print(is_palindrome("tommy"))
print(is_palindrome("alla"))
print(is_palindrome("tolik"))
print(is_palindrome("ololo"))
