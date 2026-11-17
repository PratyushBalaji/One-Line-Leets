# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# https://leetcode.com/problems/house-robber-ii/

# Beats 100% in runtime and memory!
class Solution(object):
    def rob(self, nums):
        return max(list(map(lambda arr: reduce(lambda x,y: (x[1], max(x[1], x[0]+y)), arr, (0,0))[1], [nums[1:], nums[:-1]]))+[nums[0]])
