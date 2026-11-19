# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

# https://leetcode.com/problems/max-number-of-k-sum-pairs/

# Beats 100% in runtime!
class Solution(object):
    def maxOperations(self, nums, k):
        return (lambda c: sum(min(c[i], c[k-i]) for i in [i for i in c.keys() if i > k//2]) + (c[k//2] // 2 if k%2 == 0 else 0))(Counter(i for i in nums if i < k))

# Original solution: Beats 99% in runtime!
# return (lambda c: sum(min(c[i], c[k-i]) for i in sorted(i for i in c.keys() if i > k//2)) + (c[k//2] // 2 if k%2 == 0 else 0))(Counter(i for i in nums if i < k))
