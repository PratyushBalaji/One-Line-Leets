# You are given an integer array nums of length n and an integer k.
# You need to choose exactly k non-empty subarrays (nums[l..r]) of nums. 
# Subarrays may overlap, and the exact same subarray (same l and r) can be chosen more than once.
# The value of a subarray nums[l..r] is defined as: max(nums[l..r]) - min(nums[l..r]).
# The total value is the sum of the values of all chosen subarrays.
# Return the maximum possible total value you can achieve.

# https://leetcode.com/problems/maximum-total-subarray-value-i/

# Beats 100% in Runtime!
class Solution(object):
    def maxTotalValue(self, nums, k):
        return (max(nums) - min(nums))*k