# You are given an integer array nums.
# Return the bitwise OR of all even numbers in the array.
# If there are no even numbers in nums, return 0.

# https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        return reduce(lambda x,y:x|y, filter(lambda x:x&1==0,nums) or [0])