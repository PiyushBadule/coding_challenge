# Given an array A and a number X, find a fictitious Super-Number. Here are the steps to find the Super-Number.


# e.g. For a given array A = [13, 18, 1, 3, 4, 5, 50, 29, 30, 41]

# Step-1: Find the sum of all prime numbers in an array.

#     Sum of prime numbers = 13+3+5+29+41 = 91


# Step-2: Find an absolute difference between all the elements of an original array and sum of prime numbers.

#   The elements of an array after absolute different between an element and sum of prime (ie. 91)

#   B = [ |13-91|, |18-91|, |1-91|, |3-91|,  |4-91|,  |5-91|,  |50-91|,  |29-91|,  |30-91|,  |41-91| ]

#   B = [78, 73, 90, 88, 87, 86, 41, 62, 61, 50]


# Step-3: Arrange non-prime numbers in increasing order and remove prime numbers.

#   C = [50 62 78 86 87 88 90]

#   if no, non-prime number exists, return -1.


# Step-4: Find count of sub array whose sum is less than X=200.

#   Possible sub-arrays whose sum is less than 200 are.

#   [ 50 ], [ 50, 62 ], [ 50, 62, 78 ], [ 62 ], [ 62, 78 ], [ 78 ], [ 78, 86 ], [ 86 ], [ 86, 87 ], [ 87 ], [ 87, 88 ], [ 88 ], [ 88, 90 ], [ 90 ]

#   Total sub-array are 14.


# Input

# 10
# 13 18 1 3 4 5 50 29 30 41
# 200


#     Where,

# First line represents a number of elements (N) in an array.
# Second line represents an element of an array A.
# Third line represents a value X.


# Output

# 14


# Enter Input in  Form


# Input

# 10
# 13 18 1 3 4 5 50 29 30 41
# 200


# ----------------------------------------------------------------------------------------------------------------

def solution(L, X):
    l1 = []
    z = X
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    i = 1
    count = 0
    for x in L:
        a = x
        for i in range(1, a + 1):
            if a % i == 0:
                count = count + 1

        if count == 2:
            l1.append(i)

        count = 0
        i = i + 1

    b = sum(l1)
    for x in L:
        a = x
        sub = a - b
        l2.append(abs(sub))

    l2.sort()
    for x in l2:
        a = x
        for i in range(1, a + 1):
            if a % i == 0:
                count = count + 1

        if count == 2:
            l3.append(i)
        else:
            l4.append(i)

        count = 0
        i = i + 1

    size = len(l4)
    final = 0
    for i in range(0, size):
        sum1 = 0
        for j in range(i, size):
            if (sum1 + l4[j] < z):

                sum1 = l4[j] + sum1
                final += 1
            else:
                break

    return final


N = int(input())
L = []
n = 0
for e in input().split():
    if (n < N):
        L.append(int(e))
        n += 1
X = int(input())
if (n < N):
    print("Please input {0} elements".format(N), end='')
else:
    print(solution(L, X), end='')