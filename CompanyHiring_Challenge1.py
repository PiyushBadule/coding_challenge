# Coding Challenge: Longest Common Prefix Finder
# Challenge Description:
# You are tasked with developing a function to find the longest common prefix shared among a list of strings. The common prefix must be present at the beginning of each string in the list. If no common prefix exists, your function should return an empty string.

# Examples:

# Input: ["flower","flow","flight"]
# Output: "fl"

# Input: ["dog","racecar","car"]
# Output: "" (Explanation: There is no common prefix among the input strings.)

# Constraints:

# The number of strings in the list will be between 1 and 200.
# Each string's length will range from 0 to 200.
# All strings consist only of lower-case English letters.
# Your challenge is to implement this functionality efficiently, considering the constraints and ensuring robust handling of different cases.

# Remember this challenge is from lit Code where Input is Scanned Autonatically

from typing import List

class Solution:
    def _find_common_prefix(self, str1: str, str2: str) -> str:
        """
        Helper function to find the common prefix between two strings.

        Args:
        str1 (str): The first string.
        str2 (str): The second string.

        Returns:
        str: The common prefix between str1 and str2.
        """
        min_len = min(len(str1), len(str2))

        for i in range(min_len):
            if str1[i] != str2[i]:
                return str1[:i]
        return str1[:min_len]

    def longest_common_prefix(self, strs: List[str]) -> str:
        """
        Function to find the longest common prefix string amongst an array of strings.

        Args:
        strs (List[str]): List of strings.

        Returns:
        str: The longest common prefix found. Returns an empty string if no common prefix exists.
        """
        if not strs:
            return ""
        prefix = strs[0]

        for i in range(1, len(strs)):
            prefix = self._find_common_prefix(prefix, strs[i])

        return prefix


def main():
    solution = Solution()
    print(solution.longest_common_prefix(["flower", "flow", "flight"]))  # Example 1
    print(solution.longest_common_prefix(["dog", "racecar", "car"]))     # Example 2

if __name__ == "__main__":
    main()
