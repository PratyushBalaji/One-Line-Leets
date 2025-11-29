# Given an integer n, return any array containing n unique integers such that they add up to 0.

# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

# Beats 100% in runtime
class Solution(object):
    def sumZero(self, n):
        return [i for i in range(-(n//2), (n//2) + 1) if (n%2 == 1 or i != 0)]