# The Hamming distance between two integers is the number of bit positions
# at which they differ. Given an integer array nums, return the sum of
# Hamming distances between all pairs of integers in nums.

# https://leetcode.com/problems/total-hamming-distance/

# Beats 100% in memory!
class Solution(object):
    def totalHammingDistance(self, nums):
        return (lambda l: sum((lambda s: s*(l-s))(sum((i>>x)&1 for i in nums)) for x in range(len(str(bin(max(nums))))-1)))(len(nums))
