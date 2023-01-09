def cyclops (n):
    result = str(bin(n))
    n_result = result[2:]
    if len(n_result) <= 1:
        return False
    if n_result[0:len(n_result)//2:1] == n_result[-1:len(n_result)//2:-1]:
        return True
    return False
    n = bin(n)[2:]
    return n.count('0') == 1 and n == n[::-1]

print(cyclops(5))
# stt1 = "0ba01"
# def try1(st):
#     for i in stt1:
#         mid = stt1[len(stt1)//2]
#     return mid
# stt1[slice(0,len(stt1)//2,1)]
# stt1[0:len(stt1)//2:1]
# stt1[-1:len(stt1)//2:1]
#
# # print(try1(stt1))
# print(stt1[-1:len(stt1)//2:-1])
# n = 1
# n_n = n[2:]
# result = str(bin(n))
# print(  result)
# if n[0:len(n)//2:1] == n[-1:len(n)//2:-1]:
#     print('ciclop')