# Given an array nums of non-negative integers, let rev(x) reverse the digits of x.
# A pair of indices (i, j) is nice if i < j and nums[i] + rev(nums[j]) equals
# nums[j] + rev(nums[i]). Return the number of nice pairs modulo 10^9 + 7.

# https://leetcode.com/problems/count-nice-pairs-in-an-array/

class Solution(object):
    def countNicePairs(self, nums):
        return (lambda c: sum(c[i]*(c[i]-1)//2 for i in c.keys()) % (10**9 + 7))(Counter([i-int(str(i)[::-1]) for i in nums]))
