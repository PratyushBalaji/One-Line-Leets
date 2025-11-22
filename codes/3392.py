# Given an integer array nums, return the number of subarrays of length 3 such that 
# the sum of the first and third numbers equals exactly half of the second number.

# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

class Solution(object):
    def countSubarrays(self, nums):
        return len(filter(lambda x: x[1] == (x[0]+x[2])*2,[nums[i:i+3] for i in range(len(nums)-2)]))