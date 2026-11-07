# Given an integer array nums, create a 2D array containing exactly its elements.
# Each row must contain distinct integers, and the number of rows must be minimal.
# Return any valid resulting array; rows may have different lengths.

# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution(object):
    def findMatrix(self, nums):
        return (lambda c: [[j for j in c.keys() if c[j] > i] for i in range(max(c.values()))])(Counter(nums))
