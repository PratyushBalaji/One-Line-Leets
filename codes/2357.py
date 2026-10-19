# You are given a non-negative integer array nums. In one operation, choose a
# positive integer x less than or equal to the smallest non-zero element in nums,
# and subtract x from every positive element in nums.
# Return the minimum number of operations to make every element in nums equal to 0.

# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

# Beats 100% in runtime and memory!
class Solution(object):
    def minimumOperations(self, nums):
        return 0 if max(nums) == 0 else len(set(nums)) - (1 if 0 in nums else 0)
