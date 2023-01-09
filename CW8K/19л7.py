# Complete the solution so that it
# returns true if the first argument(string) passed
# in ends with the 2nd argument (also a string).

def solution(text, ending):
    # return text[:-1-len(ending):-1] == ending[::-1]
    return text.endswith(ending)
print(solution('samurai','ai'))
ending = 'ai'
text ='samurai'
#
# print(text[:-1-len(ending):-1])
# print(ending[::-1] )