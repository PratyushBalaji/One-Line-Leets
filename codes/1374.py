# Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.
# The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  

# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution(object):
    def generateTheString(self, n):
        return 'a'*(n-1)+'b' if n%2 == 0 else 'a'*n
    
# Beats 100% in Runtime!
