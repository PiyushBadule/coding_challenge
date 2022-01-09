import sys

def smallestSumSubarr(arr, n):
    tmp = sys.maxsize

    final = sys.maxsize

    for i in range(n):
        if (tmp > 0):
            tmp = arr[i]
        else:
            tmp += arr[i]

        final = min(final, tmp)

    return final

arr = [3, -4, 2, -3, -1, 7, -5]
n = len(arr)
print("Smallest sum: ", smallestSumSubarr(arr, n))