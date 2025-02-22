# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# https://leetcode.com/problems/valid-palindrome-ii/

class Solution(object):
    def validPalindrome(self, s):
        return True in map(lambda x:x == x[::-1], [s[:i]+s[i+1:] for i in range(len(s))] + [s])
    
    
# Works in theory, but exceeds memory limit in practice since it is essentially O(n^2)