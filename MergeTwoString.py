# Description:
# Imagine you are given two strings of potentially different lengths. Your task is to create a function that merges these two strings into a new string.
# The merging process follows a specific pattern: the characters from the two strings are interwoven or alternated. 
# The first character of the first string is followed by the first character of the second string, then the second character of the first string, and so on.
# If one string is longer than the other, the remaining characters of the longer string are appended to the end of the merged string.

# Examples:

# Input:

# String 1: "abc"
# String 2: "def"
# Output: "adbecf"

# Input:

# String 1: "ab"
# String 2: "zsd"
# Output: "azbsd"

# Input:

# String 1: "zbxnsjdns"
# String 2: "idowdk"
# Output: "zibdxonwsdjkdns"

# Note: Consider edge cases such as empty strings and strings of different lengths.

def merge_strings(string1, string2):
    """
    Merges two strings into one by alternating characters from each string.
    
    If one string is longer, the remaining characters are appended at the end.
    
    Args:
    string1 (str): The first string to merge.
    string2 (str): The second string to merge.
    
    Returns:
    str: The merged string.
    """
    # Base case when one of the strings is empty
    if not string1 or not string2:
        return string1 + string2

    # Recursively merge the remaining characters
    return string1[0] + string2[0] + merge_strings(string1[1:], string2[1:])

def main():
    str1 = 'zbxnsjdns'
    str2 = 'idowdk'
    result = merge_strings(str1, str2)
    print(result)

if __name__ == "__main__":
    main()
