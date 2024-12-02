# Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.
# x mod y denotes the remainder when x is divided by y.

# https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution(object):
    def smallestEqual(self, nums):
        return ([i for i in range(len(nums)) if nums[i] == i%10]+[-1])[0]