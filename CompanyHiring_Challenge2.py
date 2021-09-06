# # Given an array of strings strs, group the anagrams together.You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# Example
# 1: Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#    Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# Example
# 2: Input: strs = [""]
#    Output: [[""]]
# Example
# 3: Input: strs = ["a"]
#    Output: [["a"]]
#
# Constraints:
#  1 <= strs.length <= 104
#  0 <= strs[i].length <= 100
#  strs[i] consists of lowercase English letters.

# Remember this challenge is from lit Code where Input is Scanned Autonatically

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        a = strs
        result = [[""]]
        if len(strs) == 0:
            return result
        else:
            for x in strs:
                l1 = str(sorted(x))
                if l1 in d:
                    d[l1].append(x)
                else:
                    d[l1] = [x]
            return list(d.values())