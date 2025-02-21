# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. 
# If there are multiple answers, you may return any of them.

# https://leetcode.com/problems/find-unique-binary-string

class Solution(object):
    def findDifferentBinaryString(self, nums):
        return ''.join('1' if nums[i][i] == '0' else '0' for i in range(len(nums)))