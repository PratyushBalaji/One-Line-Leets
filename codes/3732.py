# You are given an integer array nums.
# You must replace exactly one element in the array with any integer value in the range [-10**5, 10**5] (inclusive).
# After performing this single replacement, determine the maximum possible product of any three elements at distinct indices from the modified array.
# Return an integer denoting the maximum product achievable.

# https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

class Solution(object):
    def maxProduct(self, nums):
        return (lambda t3: 0 if t3.count(0) >= 1 else t3[0] * t3[1] * 10**5 * (1 if 0 > max(t3[0],t3[1]) or 0 < min(t3[0],t3[1]) else -1))(sorted([i[0] for i in set(heapq.nlargest(3, zip(nums,range(len(nums)))) + heapq.nsmallest(3, zip(nums,range(len(nums)))))], key=abs, reverse=True)[:2])
