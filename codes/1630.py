# An arithmetic sequence contains at least two elements with equal differences
# between consecutive elements. Given nums and range queries [l[i], r[i]],
# return whether each queried subarray can be rearranged into an arithmetic sequence.

# https://leetcode.com/problems/arithmetic-subarrays/

class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        return (lambda arith: [arith(sorted(nums[li:ri+1])) for li, ri in zip(l,r)])(lambda a: len(set([a[i] - a[i-1] for i in range(1, len(a))])) == 1)
