# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
# |x| = abs(x)

# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

class Solution(object):
    def countKDifference(self, nums, k):
        return [abs(nums[i]-nums[j])==k for i in range(len(nums)) for j in range(i+1,len(nums))].count(True)