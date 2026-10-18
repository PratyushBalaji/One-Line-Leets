# You are given an integer array nums.
# Return the smallest index i such that the sum of the digits of nums[i] is equal to i.
# If no such index exists, return -1.

# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

# Beats 100% in memory!
class Solution(object):
    def smallestIndex(self, nums):
        return next((x for x, i in enumerate(nums) if x == sum(map(int,list(str(i))))), -1)
