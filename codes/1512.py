# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is good if nums[i] == nums[j] and i < j.

# https://leetcode.com/problems/number-of-good-pairs/description/

# Beats 100% in memory!
class Solution(object):
    def numIdenticalPairs(self, nums):
        return sum(1 for i in range(len(nums)-1) for j in range(i+1, len(nums)) if nums[i]==nums[j])
