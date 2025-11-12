# You are given a positive integer n.
# Return the integer obtained by removing all zeros from the decimal representation of n.

# https://leetcode.com/problems/remove-zeros-in-decimal-representation/

class Solution(object):
    def removeZeros(self, n):
        return int(str(n).replace('0',''))