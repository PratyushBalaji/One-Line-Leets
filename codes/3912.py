# You are given an integer array nums.
# An element nums[i] is considered valid if it satisfies at least one of the following conditions:
#     It is strictly greater than every element to its left.
#     It is strictly greater than every element to its right.
# The first and last elements are always valid.
# Return an array of all valid elements in the same order as they appear in nums.

# https://leetcode.com/problems/valid-elements-in-an-array/

class Solution(object):
    def findValidElements(self, nums):
        return [i for x, i in enumerate(nums) if i > min(max(nums[:x]+[i-1]), max(nums[x+1:]+[i-1]))]
