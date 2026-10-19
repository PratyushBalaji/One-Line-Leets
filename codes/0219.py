# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j such that nums[i] == nums[j] and abs(i - j) <= k.

# https://leetcode.com/problems/contains-duplicate-ii/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        return next((True for i in range(len(nums)) for j in range(i+1, min(i+k+1, len(nums))) if nums[i] == nums[j]), False)

# Works in theory but TLE in practice.
