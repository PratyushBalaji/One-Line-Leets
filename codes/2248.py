# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, 
# return the list of integers that are present in each array of nums sorted in ascending order. 

# https://leetcode.com/problems/intersection-of-multiple-arrays/

class Solution(object):
    def intersection(self, nums):
        return sorted(reduce(lambda x,y:[i for i in x if i in y],nums))