# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one using linear time and constant extra space.

# https://leetcode.com/problems/single-number/description/

# Beats 100% in runtime and memory!
class Solution(object):
    def singleNumber(self, nums):
        return reduce(lambda x,y: x^y, nums)
