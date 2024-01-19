# Question:- Write a program to Transform input array into output array.
# Input:-[2, 4, 8, 5, 12, 15, 6, 10, 7, 30, 25, 43, 46, 45, 21]
# Output:- [2, 4, 8, 21, 12, 46, 6, 43, 7, 30, 25, 10, 15, 45, 5]

def transform_array(input_array):
    """
    Transforms the input array according to the specified rules.

    This function takes an input array and transforms it by moving all elements that are divisible by 5
    to the end of the array while keeping the relative order of other elements intact.

    Args:
        input_array (list): The input array to be transformed.

    Returns:
        list: The transformed output array.
    """
    rev_count = len(input_array)
    for i in range(len(input_array)):
        if i >= rev_count:
            break
        if input_array[i] % 5 == 0:
            replacement = 1
            while replacement != 0:
                if i >= rev_count:
                    break
                rev_count -= 1
                if input_array[rev_count] % 5 != 0:
                    input_array[i], input_array[rev_count] = input_array[rev_count], input_array[i]
                    replacement = 0
    return input_array

def main():
    input_array = [2, 4, 8, 5, 12, 15, 6, 10, 7, 30, 25, 43, 46, 45, 21]
    transformed_array = transform_array(input_array)
    print(transformed_array)

if __name__ == "__main__":
    main()
