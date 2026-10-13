# Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

# https://leetcode.com/problems/diagonal-traverse-ii/

class Solution(object):
    def findDiagonalOrder(self, nums):
        return [i[2] for i in sorted([(r+c, -r, nums[r][c]) for r in range(len(nums)) for c in range(len(nums[r]))])]
