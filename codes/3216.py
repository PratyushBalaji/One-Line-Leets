# Given a string s containing only digits, return the lexicographically smallest string 
# that can be obtained after swapping adjacent digits in s with the same parity at most once.
# Digits have the same parity if both are odd or both are even. 
# For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.

# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

class Solution(object):
    def getSmallestString(self, s):
        return min([s]+[s[:i]+s[i+1]+s[i]+s[i+2:] for i in range(len(s)-1) if int(s[i]) & 1 == int(s[i+1]) & 1])