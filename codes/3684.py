# You are given a positive integer array nums and an integer k.
# Choose at most k elements from nums so that their sum is maximized. However, the chosen numbers must be distinct.
# Return an array containing the chosen numbers in strictly descending order.

# https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements

# Beats 100% in runtime!
class Solution(object):
    def maxKDistinct(self, nums, k):
        return sorted(list(set(nums)),reverse=True)[:min(k,len(set(nums)))]