# https://leetcode.com/problems/longest-common-prefix/submissions/
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        longest_prefix = ''
        n = min([len(s) for s in strs])
        for i in range(n):
            first_chars = set([s[i] for s in strs])
            if len(first_chars) != 1:
                return longest_prefix
            else:
                longest_prefix += first_chars.pop()
        return longest_prefix