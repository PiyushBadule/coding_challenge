# Program To Reverse the Input Number and check if prime
# if X and Y is prime (X+Y)
# if X or Y is prime (A+B)
# if both are not prime (A*B)
def prime(num):
    count = 0
    for i in l1:
        num = int(i)
        for x in range(2, num):
            if num % x == 0:
                count += 1
                break
        else:
            count = 0
    return count

A, B = input().split(',')
l1 = [A[::-1], B[::-1]]
a = prime(l1)
X, Y = A[::-1],B[::-1]
if a == 0:
    print(int(X) + int(Y))
elif a == 1:
    print(int(A) + int(B))
elif a == 2:
    print(int(A) * int(B))