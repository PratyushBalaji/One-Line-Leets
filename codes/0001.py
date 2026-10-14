# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# https://leetcode.com/problems/two-sum/

# Beats 100% in memory!
class Solution(object):
    def twoSum(self, nums, target):
        return next([x, nums[x+1:].index(target-i)+x+1] for x,i in enumerate(nums) if target-i in nums[x+1:])
