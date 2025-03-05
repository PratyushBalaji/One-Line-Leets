# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# https://leetcode.com/problems/squares-of-a-sorted-array

class Solution(object):
    def sortedSquares(self, nums):
        return sorted(list(map(lambda x:x**2,nums)))