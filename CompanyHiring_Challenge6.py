# "Advanced Sequential Numeric Reduction (ASNR)"

# Given an array of integers, your task is to perform a series of operations to reduce this array to a single element through a unique process:

# Initial Reduction: Sort the array and remove duplicate elements.
# Iterative Mean Calculation:
# Repeatedly remove the first and last elements of the array.
# Calculate the mean (average) of these two elements, rounding down to the nearest integer.
# If the calculated mean is not already in the array, add it and re-sort the array.
# Termination: The process ends when only one element remains in the array.
# Your goal is to implement a function that executes this process and returns the final remaining element.

# Example:
# Input: [2, 6, 1, 1, 7, 8, 8, 8]
# Output: 5

def advanced_sequential_numeric_reduction(numbers):
    """
    Perform the Advanced Sequential Numeric Reduction (ASNR) on a list of integers.

    Args:
    numbers (list): A list of integers.

    Returns:
    int: The final remaining number after performing ASNR.
    """
    # Remove duplicates and sort the list
    unique_numbers = sorted(set(numbers))

    # Continue the process until only one element remains
    while len(unique_numbers) > 1:
        first, last = unique_numbers[0], unique_numbers[-1]
        unique_numbers.pop(0)
        unique_numbers.pop(-1)
        mean = (first + last) // 2

        if mean not in unique_numbers:
            unique_numbers.append(mean)
            unique_numbers.sort()

    # Return the remaining element
    return unique_numbers[0]

# Test the function
if __name__ == "__main__":
    input_array = [2, 6, 1, 1, 7, 8, 8, 8]
    result = advanced_sequential_numeric_reduction(input_array)
    print("Final result:", result)
