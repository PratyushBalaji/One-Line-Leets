# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# https://leetcode.com/problems/missing-number/

class Solution(object):
    def missingNumber(self, nums):
        return (reduce(lambda x,y:x^y,nums + [reduce(lambda x,y:x^y,range(len(nums)+1))]))
