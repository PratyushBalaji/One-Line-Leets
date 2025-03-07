# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# https://leetcode.com/problems/valid-palindrome-ii/

class Solution(object):
    def validPalindrome(self, s):
        # return True in map(lambda x:x == x[::-1], [s[:i]+s[i+1:] for i in range(len(s))] + [s])
        return next((True for i in range(len(s)) if s[:i] + s[i+1:] == (s[:i] + s[i+1:])[::-1]), s == s[::-1])

    
    
# Solution 1 works in theory, but exceeds memory limit in practice since it is essentially O(n^2)
# Solution 2 works in theory, and optimises memory by using a generator, but exceeds time limit in practice