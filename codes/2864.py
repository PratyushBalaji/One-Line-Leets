# You are given a binary string s that contains at least one '1'.
# You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.
# Return a string representing the maximum odd binary number that can be created from the given combination.
# Note that the resulting string can have leading zeros.

# https://leetcode.com/problems/maximum-odd-binary-number/

class Solution(object):
    def maximumOddBinaryNumber(self, s):
        return "1"*(s.count("1")-1) + "0"*s.count("0") + "1"