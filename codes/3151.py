# An array is considered special if the parity of every pair of adjacent elements is different. 
# In other words, one element in each pair must be even, and the other must be odd.
# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

# https://leetcode.com/problems/special-array-i

class Solution(object):
    def isArraySpecial(self, nums):
        return all(a != b for a, b in zip(map(lambda x: x % 2, nums), map(lambda x: x % 2, nums)[1:]))