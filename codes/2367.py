# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. 
# A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
#     i < j < k,
#     nums[j] - nums[i] == diff, and
#     nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

# https://leetcode.com/problems/number-of-arithmetic-triplets/

# Beats 100% in runtime and memory!
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        return (lambda numset: sum([1 for i in numset if i+diff in numset and i+diff+diff in numset]))(set(nums))