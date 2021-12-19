# Question:- Write a program to Transform input array into output array.
# Input:-[2, 4, 8, 5, 12, 15, 6, 10, 7, 30, 25, 43, 46, 45, 21]
# Output:- [2, 4, 8, 21, 12, 46, 6, 43, 7, 30, 25, 10, 15, 45, 5]
a = [2, 4, 8, 5, 12, 15, 6, 10, 7, 30, 25, 43, 46, 45, 21]
rev_count = len(a)
for i in range(len(a)):
    if (i>rev_count):
        break
    if (a[i]%5 == 0):
        replacement = 1
        while replacement != 0:
            if (i >= rev_count):
                break
            rev_count -= 1
            if (a[rev_count]%5 != 0):
                temp = a[i]
                a[i] = a[rev_count]
                a[rev_count] = temp
                replacement = 0
print(a)