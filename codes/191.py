# Given a positive integer n, write a function that returns the number of set bits in its binary representation.
# (also known as the Hamming weight)

# https://leetcode.com/problems/number-of-1-bits/

class Solution(object):
    def hammingWeight(self, n):
        return str(bin(n)).count("1")