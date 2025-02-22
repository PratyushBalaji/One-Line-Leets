# Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.

# https://leetcode.com/problems/remove-trailing-zeros-from-a-string

class Solution(object):
    def removeTrailingZeros(self, num):
        return num[::-1][[0 if i == '0' else 1 for i in num[::-1]].index(1):][::-1]