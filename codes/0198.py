# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# https://leetcode.com/problems/house-robber/

# Beats 100% in runtime and memory!
class Solution(object):
    def rob(self, nums):
        return reduce(lambda x,y: (x[1], max(x[1], x[0]+y)), nums, (0,0))[1]
