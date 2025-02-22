# Reverse bits of a given 32 bits unsigned integer.

# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n):
        return int(('0'*(32-len(str(bin(n)[2:]))) + str(bin(n)[2:]))[::-1],2)