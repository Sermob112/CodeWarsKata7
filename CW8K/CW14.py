# Every budding hacker needs an alias! The Phantom Phreak, Acid Burn, Zero Cool and Crash Override are some notable examples
# from the film Hackers.
#
# Your task is to create a function that, given a proper first and last name, will return the correct alias.
#
# Notes:
# Two objects that return a one word name in response to the first letter of the first name and one for
#     the first letter of the surname are already given. See the examples below for further details.
#
# If the first character of either of the names given to the function is not a letter
# from A - Z, you should return "Your name must start with a letter from A - Z."
#
# Sometimes people might forget to capitalize the first letter of their name so your function
# should accommodate for these grammatical errors.



# My attempt
FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache'}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst', 'P':'PlayLoad' }
# def alias_gen(f_name,l_name):
#     new_name = []
#     str_b = 'Your name must start with a letter from A - Z.'
#     if(f_name[0].isdigit() or l_name[0].isdigit()):
#         return  str_b
#     for i in FIRST_NAME:
#         if(f_name[0].title() == i ):
#             new_name.append(FIRST_NAME[i])
#     for j in SURNAME:
#         if (l_name[0].title() == j):
#             new_name.append(SURNAME[j])
#     str_a = ' '.join(new_name)
#     return str_a
# print(alias_gen('abc','Pinkman'))
#Best cleaver
def alias_gen(f_name,l_name):
    try:
        return FIRST_NAME[f_name.upper()[0]] +' '+ SURNAME[l_name.upper()[0]]
    except:
        return  'Your name must'

print(alias_gen('abc','Pinkman'))
# str = 'peps'
# print(str[0].title())