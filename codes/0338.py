# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# https://leetcode.com/problems/counting-bits/

class Solution(object):
    def countBits(self, n):
        return [sum([(j >> i) & 1 for i in range(len(str(bin(j))) - 2)]) for j in range(n+1)]