# Problem Statement: Contiguous Subarray with Smallest Sum

# You are given an array of integers. Your task is to find the contiguous subarray within the array that has the smallest sum of its elements. 
This problem is a classic example in computer science and is frequently encountered in various technical interviews.
# Write a Python function find_smallest_sum_subarray(arr: List[int]) -> int that takes in an array of integers arr and returns the smallest sum contiguous subarray.
# For example, given the array arr = [3, -4, 2, -3, -1, 7, -5], the smallest sum contiguous subarray is [-4, 2, -3, -1] with a sum of -6.
# Your solution should handle arrays of arbitrary lengths and negative numbers efficiently.

# Function Signature:
# def find_smallest_sum_subarray(arr: List[int]) -> int:
    # Your code here

# Constraints:

# The length of the input array arr will be between 1 and 10^5.
# Each element of the array will be an integer between -1000 and 1000.
# Example:
# >>> find_smallest_sum_subarray([3, -4, 2, -3, -1, 7, -5])
# -6

# Evaluation Criteria:
# Correctness of the solution
# Efficiency of the algorithm (time and space complexity)
# Code readability and adherence to Python coding standards
    
def smallest_sum_subarray(arr):
    """
    Finds the smallest sum contiguous subarray within the given array.

    Parameters:
    arr (list): The input array.

    Returns:
    int: The smallest sum contiguous subarray.
    """
    tmp = float('inf')
    final = float('inf')

    for num in arr:
        if tmp > 0:
            tmp = num
        else:
            tmp += num
        final = min(final, tmp)

    return final

def main():
    arr = [3, -4, 2, -3, -1, 7, -5]
    print("Smallest sum: ", smallest_sum_subarray(arr))

if __name__ == "__main__":
    main()
