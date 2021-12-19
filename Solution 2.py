# Question:- You have to write a program to transform input array into output array.
# Input Array :  2,4,8,5,12,15,6,10,7,30,25,43,46,45,21
# Output Array :  2,4,8,12,6,7,43,46,21,5,15,10,30,25,45
# Do not use duplicate or extra array.
# Hint: All multiples of 5 are moved to last

a = [2, 4, 8, 5, 12, 15, 6, 10, 7, 30, 25, 43, 46, 45, 21]
j = 0; b = len(a)
for x in range (0, b):
    if (a[x]%5 == 0):
        a.append(a[x])
for y in range(0, b):
    if (a[j]%5 == 0):
        a.remove(a[j])
        j -= 1
    j += 1
print(a)