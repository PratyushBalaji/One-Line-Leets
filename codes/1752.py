# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). 
# Otherwise, return false.
# There may be duplicates in the original array.
# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

class Solution(object):
    def check(self, nums):
        return (lambda i: nums[i:] + nums[:i] == sorted(nums))((next((i for i in range(1, len(nums)) if nums[i] < nums[i-1]), 0)))