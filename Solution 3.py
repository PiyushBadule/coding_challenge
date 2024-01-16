# Question:-  Let's say you are given a string. You can get many strings (combination)
# out of the given original string if you rearrange characters of original string.
# String is Palindromable if any one combination is palindrome.
# Example 1:
# Original String: NINIT
# Combinations: NINIT, NNIIT,IINNT,ININT,IITNN,NITIN,INTIN,INTNI,NTNII,NNTII and so on
# Original string is  Palindromable because two palindrome can be made out of it.
# Example 2:
# Original String: NINNIT
# Combinations: NINITN, NNINIT,IINNNT,INNINT,INITNN,NNITIN,INTNIN,INTNIN,NTNINI,NNTINI and so on
# Original string is NOT Palindromable because NO palindrome can be made out of it.
# Write a program to check it given string is Palindromable or not. (please note this is not a
# question to check if string is palindrome or not).
# (Hint: Do not write a program to find the permutation and combination of original string and then
# check combination. Program is much simpler than finding permutation and combination. )

def is_palindromable(s):
    """
    Checks if the given string can be rearranged to form a palindrome.

    Args:
    s (str): The string to be checked.

    Returns:
    bool: True if the string can be rearranged to form a palindrome, False otherwise.
    """
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)

    return odd_count <= 1

def main():
    """
    Main function to drive the program. Takes a string as input and checks if it is Palindromable.
    """
    input_string = input("Enter a string: ")
    if is_palindromable(input_string):
        print("Palindromable")
    else:
        print("NOT Palindromable")

if __name__ == "__main__":
    main()
