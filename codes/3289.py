# You are given a list of numbers containing integers from 0 to n-1
# There are exactly two numbers that appear twice in the list
# Find the two numbers that appear twice and return them as a list in any order

# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

class Solution(object):
    def getSneakyNumbers(self, nums):
        return list(set(i for i in nums if nums.count(i) == 2))