# Question:- You have an array of length N which have some two digit numbers in it.
# Each number is only occurring once. You have to find out count of those number
# which have their reverse number present.
# Do not use Two Nested Loops
# Example :
# Input:- [21, 43, 54, 23, 67, 90, 84, 34, 45, 55, 76, 26, 48, 52, 25]
# Output:- 4

def count_reverse_pairs(array):
    """
    Counts the number of elements in the array that have their reverse also present in the array.
    Each element is considered only once for a pair.

    Parameters:
    array (list of int): A list of integers.

    Returns:
    int: The count of elements which have their reverse present in the array.
    """
    count = 0
    checked_elements = []

    for element in array:
        checked_elements.append(element)
        reversed_element = int(str(element)[::-1])

        # Skip if reversed element is already checked
        if reversed_element in checked_elements:
            continue

        # Increment count if reversed element is found in array
        if reversed_element in array:
            count += 1

    return count

if __name__ == "__main__":
    arr = [21, 43, 54, 23, 67, 90, 84, 34, 45, 55, 76, 26, 48]
    result = count_reverse_pairs(arr)
    print(result)
