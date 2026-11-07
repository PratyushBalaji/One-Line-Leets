# Given an array nums of even length, pair up all elements so each appears in
# exactly one pair. A pair's sum is the sum of its two elements.
# Return the smallest possible maximum pair sum over all such pairings.

# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

# Beats 100% in runtime and memory!
class Solution(object):
    def minPairSum(self, nums):
        return (lambda n, l: max([n[i]+n[l-i-1] for i in range(l//2)]))(sorted(nums), len(nums))
