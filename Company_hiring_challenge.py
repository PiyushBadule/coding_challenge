# "Advanced Super-Number Array Transformation Challenge"
# Introduction

# In the realm of data manipulation and algorithmic challenges, the task of array transformation stands as a cornerstone of computational problem-solving. This challenge invites you to delve into the intricate world of arrays, prime number analysis, and dynamic sub-array calculations.

# Objective

# Your mission, should you choose to accept it, involves a sophisticated operation on an integer array A, coupled with a numerical limit X. Your task is to compute a value known as the "Super-Number" through a multi-stage transformation process. Each stage requires a blend of mathematical acumen and algorithmic precision.

# Transformation Stages

# Prime Enumeration: Traverse through array A and compute the aggregate of all prime elements. This total is your "Prime Summation".

# Differential Mapping: Construct an array B, each of whose elements represents the absolute disparity between the corresponding element in A and the "Prime Summation".

# Selective Ordering: Rearrange array B in an ascending sequence, meticulously excluding all prime numbers from this ordered collection.

# Sub-Array Stratagem: Engage in a counting operation to identify all possible sub-arrays within the sorted, non-prime array B, ensuring that the sum of elements in each sub-array does not exceed the threshold X.

# Exceptional Handling: In a scenario where array B is devoid of non-prime numbers, declare the "Super-Number" as -1.

# Input Specifications

# The first line of input represents the count of elements N in array A.
# The second line contains N space-separated integers, delineating array A.
# The third line specifies the numerical limit X.
# Output Specifications

# Output a single integer - the calculated "Super-Number".

# Example 1:
# Enter number of elements: 10
# Enter exactly 10 elements, separated by spaces: 13 18 1 3 4 5 50 29 30 41
# Enter the value of X: 200

# Super-Number: 14

# Example 2:
# Enter number of elements: 5
# Enter exactly 5 elements, separated by spaces: 2 3 5 7 11
# Enter the value of X: 10

# Super-Number: -1

def count_subarrays(arr, limit):
    """
    Calculate the count of subarrays where the sum of elements is less than the given limit.

    Args:
    arr (list): A list of integers.
    limit (int): The upper limit for the sum of subarray elements.

    Returns:
    int: Count of subarrays satisfying the condition.
    """
    count = 0
    for start in range(len(arr)):
        sum = 0
        for end in range(start, len(arr)):
            sum += arr[end]
            if sum < limit:
                count += 1
            else:
                break
    return count

def is_prime(n):
    """
    Check if a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def super_number_finder(arr, X):
    """
    Determine the Super-Number based on the given array transformation process.

    Args:
    arr (list): An array of integers.
    X (int): The upper limit for the sum of subarray elements.

    Returns:
    int: The Super-Number based on the array transformation.
    """
    # Step 1: Sum of prime numbers
    prime_sum = sum([num for num in arr if is_prime(num)])

    # Step 2: Absolute difference array
    diff_arr = [abs(num - prime_sum) for num in arr]

    # Step 3: Sort non-prime numbers
    non_prime_sorted = sorted([num for num in diff_arr if not is_prime(num)])

    # Return -1 if no non-prime numbers
    if not non_prime_sorted:
        return -1

    # Step 4: Count sub-arrays
    return count_subarrays(non_prime_sorted, X)

# Main block to test the function
if __name__ == "__main__":
    try:
        N = int(input("Enter number of elements: "))
        elements = input(f"Enter exactly {N} elements, separated by spaces: ").split()

        if len(elements) != N:
            print(f"Please input exactly {N} elements")
        else:
            A = list(map(int, elements))
            X = int(input("Enter the value of X: "))
            print("Super-Number:", super_number_finder(A, X))
    except ValueError:
        print("Please enter valid integer values.")
