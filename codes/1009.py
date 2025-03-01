# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
#     For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer n, return its complement.

# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution(object):
    def bitwiseComplement(self, n):
        return int(''.join(['0' if i=='1' else '1' for i in str(bin(n))[2:]]),2)