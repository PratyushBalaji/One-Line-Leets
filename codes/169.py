# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# https://leetcode.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums):
        return max(set(nums),key=nums.count)