# The Collatz Conjecture states that for
#     any positive natural number n, this process:
#
# if n is even, divide it by 2
# if n is odd, multiply it by 3 and add 1
# repeat
# will eventually reach n = 1.
#
# For example, if n = 20, the resulting sequence will be:
# [ 20, 10, 5, 16, 8, 4, 2, 1 ]
def collatz(n):
    i = 1
    if(n % 2 == 0):
        while(n % 2 == 0):
            n = n / 2
            i += 1
            if (n == 1):
                break
            while (n % 2 !=0):
                n = n * 3 + 1
                i += 1
                if(n == 1):
                    break
    else:
        while (n % 2 != 0):
            if (n == 1):
                break

            n = n * 3 + 1
            i += 1
            while (n % 2 == 0):
                if (n == 1):
                    break
                n = n / 2
                i += 1

    return i
print(collatz(73567465519280238573))