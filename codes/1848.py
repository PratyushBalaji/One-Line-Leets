# Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. 
# Note that abs(x) is the absolute value of x.
# Return abs(i - start).
# It is guaranteed that target exists in nums.

# https://leetcode.com/problems/minimum-distance-to-the-target-element/

class Solution(object):
    def getMinDistance(self, nums, target, start):
        return min([abs(start-x) for x, i in enumerate(nums) if i == target])
