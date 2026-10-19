# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.

# https://leetcode.com/problems/contains-duplicate/description/

# Python 2: filter() returns a list.
class Solution(object):
    def containsDuplicate(self, nums):
        return bool(filter(lambda x: x > 1, Counter(nums).values()))
