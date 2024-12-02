# You are given a positive integer array nums.
#     The element sum is the sum of all the elements in nums.
#     The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.
# Note that the absolute difference between two integers x and y is defined as |x - y|.

# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution(object):
    def differenceOfSum(self, nums):
        return abs(sum(map(lambda x: sum([int(i) for i in str(x)]),nums)) - sum(nums))