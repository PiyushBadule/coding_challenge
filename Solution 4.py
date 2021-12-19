# Question:- You have an array of length N which have some two digit numbers in it.
# Each number is only occurring once. You have to find out count of those number
# which have their reverse number present.
# Do not use Two Nested Loops
# Example :
# Input:- [21, 43, 54, 23, 67, 90, 84, 34, 45, 55, 76, 26, 48, 52, 25]
# Output:- 4
arr = [21, 43, 54, 23, 67, 90, 84, 34, 45, 55, 76, 26, 48]
count = 0
checked = []
for i in arr:
    checked.append(i)
    a = int(str(i)[::-1])
    if a in checked:
        continue
    if a in arr:
        count += 1
print(count)