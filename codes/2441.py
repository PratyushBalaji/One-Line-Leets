# Given an integer array nums containing no zeros, find the largest positive
# integer k such that -k also exists in the array. Return -1 if none exists.

# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/

class Solution(object):
    def findMaxK(self, nums):
        return max([i for i in nums if i > 0 and -i in nums]+[-1])
