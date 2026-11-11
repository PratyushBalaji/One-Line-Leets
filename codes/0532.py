# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
#     0 <= i, j < nums.length
#     i != j
#     |nums[i] - nums[j]| == k
# Notice that |val| denotes the absolute value of val.

# https://leetcode.com/problems/k-diff-pairs-in-an-array/

# Beats 100% in memory!
class Solution(object):
    def findPairs(self, nums, k):
        return (lambda s: sum(1 for i in s if nums.count(i) > 1) if k == 0 else sum((1 if i+k in s else 0)+(1 if i-k in s else 0)-(1 if i+k == i-k else 0) for i in s) // 2)(set(nums))
