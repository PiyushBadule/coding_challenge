# Input:- [2, 6, 1, 1, 7, 8, 8, 8]
# Output:- 5
# Sort the array with unique values
# Take the mean from first and last number then after taking mean if that value is not present add
# that number to array and again take the mean till the last element lest on array
A = [2, 6, 1, 1, 7, 8, 8, 8]
N = 8
a = sorted(list(set(A)))
length = len(a)
while length != 1:
    a.pop(0)
    a.pop(len(a)-1)
    res = a[0] + a[-1]
    res = int(res / 2)
    length = len(a)
    if res not in a:
        a.append(res)
        a.sort()

else:
    res = a[0]

print(res)