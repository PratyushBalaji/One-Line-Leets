# You are given an integer array nums.
# Return the smallest absent positive integer in nums such that it is strictly greater than the average of all elements in nums.
# The average of an array is defined as the sum of all its elements divided by the number of elements. 

# https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

class Solution(object):
    def smallestAbsent(self, nums):
        return next(i for i in range(max(int(sum(nums) / len(nums)) + 1, 1), max(nums+[1]) + 2) if i not in set(nums))