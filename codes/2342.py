# You are given a 0-indexed array nums consisting of positive integers.
# You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].
# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.
# If no such pair of indices exists, return -1.

# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

class Solution(object):
    def maximumSum(self, nums):
        return (lambda d: max([i+d[sum(map(int, str(i)))][0] for x, i in enumerate(sorted(nums)[::-1]) if d[sum(map(int, str(i)))][1] != x] + [-1]))({sum(map(int, list(str(i)))):(i,len(nums)-x-1) for x, i in enumerate(sorted(nums))})
