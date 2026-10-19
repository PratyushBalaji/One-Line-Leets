# You are given an integer array nums and two integers indexDiff and valueDiff.
# Find a pair of indices (i, j) such that i != j, abs(i - j) <= indexDiff,
# and abs(nums[i] - nums[j]) <= valueDiff.
# Return true if such a pair exists or false otherwise.

# https://leetcode.com/problems/contains-duplicate-iii/description/

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        return next((True for i in range(len(nums)) for j in range(i+1, min(len(nums), i+indexDiff+1)) if abs(nums[i]-nums[j]) <= valueDiff), False)

# Works in theory but TLE in practice.
