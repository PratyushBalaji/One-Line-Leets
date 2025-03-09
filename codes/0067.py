# Given two binary strings a and b, return their sum as a binary string.

# https://leetcode.com/problems/add-binary

class Solution(object):
    def addBinary(self, a, b):
        return str(bin(int(a,2) + int(b,2)))[2:]