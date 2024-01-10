# Problem Statement: Advanced Anagram Grouping
# Objective:
# Develop an efficient algorithm to categorize a collection of strings into groups of anagrams. 
# An anagram is defined as a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

# Input:

# A list of strings, strs, where each string consists of lowercase English letters.
# The length of strs is between 1 and 10^4, inclusive.
# Each string in strs has a length between 0 and 100, inclusive.
# Output:

# A list of lists, where each inner list contains strings that are anagrams of each other.
# The grouping of anagrams does not need to be ordered.
# Examples:

# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# Input: strs = [""]
# Output: [[""]]
# Input: strs = ["a"]
# Output: [["a"]]

# Remember this challenge is from lit Code where Input is Scanned Autonatically

from typing import List
from collections import defaultdict

class AnagramGrouper:
    """
    A class to group a list of strings into anagrams.

    Methods:
    group_anagrams(strs) -> List[List[str]]:
        Groups the given strings into lists of anagrams.
    """

    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups the given strings into lists of anagrams.

        Parameters:
        strs (List[str]): A list of strings.

        Returns:
        List[List[str]]: A list of lists, where each inner list contains anagrams.
        """
        if not strs:
            return [[""]]

        anagram_dict = defaultdict(list)
        for word in strs:
            sorted_word = str(sorted(word))
            anagram_dict[sorted_word].append(word)

        return list(anagram_dict.values())

# Example usage
if __name__ == "__main__":
    ag = AnagramGrouper()
    example_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(ag.group_anagrams(example_strs))
