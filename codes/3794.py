# You are given a string s and an integer k.
# Reverse the first k characters of s and return the resulting string.

# https://leetcode.com/problems/reverse-string-prefix/

# Beats 100% in runtime and memory!
class Solution(object):
    def reversePrefix(self, s, k):
        return s[:k][::-1] + s[k:]
