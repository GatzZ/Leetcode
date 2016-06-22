# coding=utf-8
# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
#  "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        best_len = 0
        start = 0
        char_idx = {}
        for i in xrange(len(s)):
            if s[i] in char_idx and start <= char_idx[s[i]]:
                start = char_idx[s[i]] + 1
            else:
                best_len = max(best_len, i - start + 1)
            char_idx[s[i]] = i
        return best_len


s = "abcabcbb"
# s = "bbbbb"
s = "pwwkew"
print Solution().lengthOfLongestSubstring(s)
