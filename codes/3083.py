# Given a string s, find any substring of length 2 which is also present in the reverse of s.
# Return true if such a substring exists, and false otherwise.

# https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

class Solution(object):
    def isSubstringPresent(self, s):
        return True in [s[i:i+2] in s[::-1] for i in range(len(s)-1)]