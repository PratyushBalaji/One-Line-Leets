# Given an integer array of size n, find all elements that appear more than ⌊n/3⌋ times.

# https://leetcode.com/problems/majority-element-ii/ 

class Solution(object):
    def majorityElement(self, nums):
        return [i for i in set(nums) if nums.count(i) > len(nums)//3]