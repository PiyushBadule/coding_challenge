# Merge the two string
# Input:- a = "abc"
#         b = "def"
# Output:- adbecf
#
# Input:- a = "ab"
#         b = "zsd"
# Output:- azbsd
#
# Input:- a = "zbxnsjdns"
#         b = "idowdk"
# Output:- zibdxonwsdjkdns

str1 = 'zbxnsjdns'
str2 = 'idowdk'


def merge(str1, str2):
    if len(str1) == 0:
        return str1 + str2
    return str1[:1] + str2[:1] + merge(str1[1:], str2[1:])


str1 = list(str1)
str2 = list(str2)
x = merge(str1, str2)
print(''.join(x))