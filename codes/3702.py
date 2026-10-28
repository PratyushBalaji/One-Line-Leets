# You are given an integer array nums.
# Return the length of the longest subsequence whose bitwise XOR is non-zero.
# If no such subsequence exists, return 0.

# https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

class Solution(object):
    def longestSubsequence(self, nums):
        return len(nums) if reduce(lambda x,y:x^y, nums) else next((len(nums)-1 for i in nums if i != 0), 0)
