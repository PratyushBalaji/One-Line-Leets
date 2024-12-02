# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

# https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution(object):
    def hasAlternatingBits(self, n):
        return not False in [False for i in range(1,len(str(bin(n))[2:])) if str(bin(n))[2:][i-1]==str(bin(n))[2:][i]]
    
# Beats 100% in Runtime!