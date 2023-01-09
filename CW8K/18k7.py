# Task
# Given a string str, reverse it and omit all non-alphabetic characters.
#
# Example
# For str = "krishan", the output should be "nahsirk".
#
# For str = "ultr53o?n", the output should be "nortlu".
#
# Input/Output
# [input] string str
# A string consists of lowercase latin letters, digits and symbols.
#
# [output] a string
def reverse_letter(string):
    new_s = ''.join(c for c in string if c.isalnum() and not c.isdigit())[::-1]
    return new_s
# str1 = "ultr53o?n"
# sim = ['1234567890!@#$%^&*()_-+']
# gug = ''.join(c for c in str1 if c.isalnum() and not c.isdigit())
#
# str2 = str1.replace('1234567890!@#$%^&*()_-+','')
# print(gug)
print(reverse_letter("krishan"))

