
# Write a function consonantCount, consonant_count or ConsonantCount
# that takes a string of English-language text and returns the number of consonants in the string.
#
# Consonants are all letters used to write English excluding the vowels a, e, i, o, u.
str1 = 'RfMRFyIwJNhiKlWtqXpwrIJUpg'
glast = ['m','q','x','b','f','j','n','r','v','c','g','k','s','w','z','d','h','l','p','t','y']
def consonant_count(s):
    i = 0
    for j in s:
        for k in glast:
            if(j.upper() == k.upper()):
               i += 1
    return i
    return sum(1 for c in str if c.isalpha() and c.lower() not in "aeiou")
    return len([i for i in s.lower() if i in 'bcdfghjklmnpqrstvwxyz'])
print(consonant_count(str1))