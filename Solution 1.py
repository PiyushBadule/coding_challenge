# Coding Challenge: Reverse Word Order in a Sentence
# Task: Write a function reverse_word_order that takes a sentence as input and reverses the order of the words in the sentence. Each word should remain in its original form, but the order of words should be reversed. The solution must not use library functions like split for splitting the sentence into words.

# Input: A string sentence representing the sentence to be processed.

# Output: A string representing the sentence with the word order reversed.

# Constraints:

# Do not use any built-in library functions like split for manipulating the sentence.
# Consider only spaces as word separators.
# Preserve the original form of each word.
# Assume the input string does not have leading or trailing spaces and the words are separated by a single space.
# Example:

# Input: "I Love my India"
# Output: "India my Love I"
# Solution:

def reverse_word_order(sentence):
    """
    Reverses the order of words in a given sentence without using library functions like split or reversed.

    Args:
    sentence (str): The sentence to be processed.

    Returns:
    str: The sentence with the order of words reversed.
    """
    words = []
    word = ''
    for char in sentence:
        if char != ' ':
            word += char
        else:
            if word:
                words.insert(0, word)  # Insert the word at the beginning of the list
                word = ''
    if word:  # To add the last word if it exists
        words.insert(0, word)

    reversed_sentence = ' '.join(words)
    return reversed_sentence

def main():
    """
    Main function to drive the program. It takes a sentence as input and outputs it with the words reversed.
    """
    sentence = input("Enter a sentence: ")
    reversed_sentence = reverse_word_order(sentence)
    print("Reversed Sentence:", reversed_sentence)

if __name__ == "__main__":
    main()
