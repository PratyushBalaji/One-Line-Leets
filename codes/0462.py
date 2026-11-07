# Given an integer array nums, return the minimum number of moves required to
# make all elements equal. Each move increments or decrements one element by 1.
# The answer fits in a 32-bit integer.

# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

class Solution(object):
    def minMoves2(self, nums):
        return (lambda m: sum(map(lambda x: abs(x-m), nums)))(sorted(nums)[len(nums)//2])
