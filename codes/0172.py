# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

# https://leetcode.com/problems/factorial-trailing-zeroes/

# Beats 100% in runtime!
class Solution(object):
    def trailingZeroes(self, n):
        return sum(n//(5**i) for i in range(1, next(i for i in count() if 5**i > n)))
