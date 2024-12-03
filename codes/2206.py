# You are given an integer array nums consisting of 2 * n integers.
# You need to divide nums into n pairs such that:
#     Each element belongs to exactly one pair.
#     The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.

# https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution(object):
    def divideArray(self, nums):
        return not 1 in [nums.count(i)%2 for i in set(nums)]