# Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
# If there are multiple answers, return the number with the largest value.

# https://leetcode.com/problems/find-closest-number-to-zero

class Solution(object):
    def findClosestNumber(self, nums):
        return -min(map(lambda x:(abs(x - 0),-x),nums))[1]