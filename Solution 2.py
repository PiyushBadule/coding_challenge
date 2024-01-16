# Coding Challenge: Array Transformation Based on Multiples of 5
# Task: Write a function transform_array that modifies an input array in-place such that all elements that are multiples of 5 are moved to the end of the array.
# The order of the non-multiples of 5 should remain unchanged, and the order of the multiples of 5 at the end of the array is not important.
# This transformation must be done without using any extra or duplicate arrays.

# Input: An array of integers.

# Output: The same array, modified according to the specified conditions.

# Constraints:

# Do not use any additional arrays for storing elements.
# Preserve the original order of non-multiples of 5.
# The function should modify the array in-place.
# Assume the input array contains only integers.
# Example:

# Input Array: [2, 4, 8, 5, 12, 15, 6, 10, 7, 30, 25, 43, 46, 45, 21]
# Output Array: [2, 4, 8, 12, 6, 7, 43, 46, 21, 5, 15, 10, 30, 25, 45]
# Solution:

def transform_array(arr):
    """
    Transforms the given array such that all elements that are multiples of 5 
    are moved to the end of the array. The order of non-multiples of 5 should remain 
    unchanged, while the order of the multiples of 5 at the end is not important.
    This function modifies the array in-place.

    Args:
    arr (list): The array to be transformed.

    Returns:
    None: The array is modified in-place.
    """
    insert_pos = 0
    for i in range(len(arr)):
        if arr[i] % 5 != 0:
            arr[insert_pos], arr[i] = arr[i], arr[insert_pos]
            insert_pos += 1

def main():
    """
    Main function to drive the program. Takes an array, transforms it and prints the result.
    """
    array = [2, 4, 8, 5, 12, 15, 6, 10, 7, 30, 25, 43, 46, 45, 21]
    print("Original Array:", array)
    transform_array(array)
    print("Transformed Array:", array)

if __name__ == "__main__":
    main()
