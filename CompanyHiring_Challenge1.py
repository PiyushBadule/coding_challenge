# Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

# Remember this challenge is from lit Code where Input is Scanned Autonatically

class Solution:
    def longSeq(self, str1, str2) -> str:
        l1 = len(str1)
        l2 = len(str2)
        res = ""
        minLen = min(l1, l2)

        if minLen == 1:
            if str1[0] == str2[0]:
                return str1[0]
            else:
                return ""
        else:
            for i in range(0, minLen):
                if (str1[i] != str2[i]):
                    break
                else:
                    res = res + str1[i]

                # i +=1
                # j += 1
            return res

    def longestCommonPrefix(self, strs: List[str]) -> str:
        l1 = strs[0]

        prefix = l1
        if len(l1) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:

            for i in range(1, len(strs)):
                # pre+fix1 = self.longSeq(l1, strs[i])
                prefix = self.longSeq(prefix, strs[i])

            return prefix