# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
def spinWords(str1):
    # new_s = [(c for c in str1 if len(c) > 4)][::-1]
    end = []
    new_s =  str1.split(' ')
    for c in new_s:
        if len(c) < 5:
            end.append(c)

        else:
            c = ''.join(i for i in c)[::-1]
            end.append(c)
    endstr = ' '.join(i for i in end)
    return " ".join([x[::-1] if len(x) >= 5 else x for x in str1.split(" ")])
    return endstr

print(spinWords('Hey fellow warriors'))