# You are given an integer array nums of size n. Return the minimum number of
# moves required to make all elements equal. Each move increments n - 1 elements by 1.

# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

# Beats 100% in runtime!
class Solution(object):
    def minMoves(self, nums):
        return sum(nums) - min(nums)*len(nums)
        # return (lambda m: sum(map(lambda x: x-m, nums)))(min(nums))
