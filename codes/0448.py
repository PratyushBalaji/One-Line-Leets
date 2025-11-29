# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution(object):
    def findDisappearedNumbers(self, nums):
        return (lambda s: [i for i in range(1,len(nums)+1) if i not in s])(set(nums))