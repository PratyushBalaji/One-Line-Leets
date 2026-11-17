# Given an integer array nums and an integer k, return the smallest positive multiple of k that is missing from nums.
# A multiple of k is any positive integer divisible by k.

# https://leetcode.com/problems/smallest-missing-multiple-of-k/

class Solution(object):
    def missingMultiple(self, nums, k):
        return (lambda s: next(i for i in count(k,k) if i not in s))(set(nums))
