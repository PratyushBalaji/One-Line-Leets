# You are given an integer array nums and an integer k.
# In the K-or operation, a result bit is set if at least k numbers in nums have
# that bit set. Return the K-or of nums.

# https://leetcode.com/problems/find-the-k-or-of-an-array/

class Solution(object):
    def findKOr(self, nums, k):
        return (lambda counts: sum(1<<x for x, i in enumerate(counts) if i >= k))([sum(1 for n in nums if n & (1<<x)) for x in range(len(str(bin(max(nums)))) - 1)])
