# You are given an integer array nums. You may rearrange the elements in any order.
# The alternating score of an array arr is defined as:
#     score = arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + ...
# Return an integer denoting the maximum possible alternating score of nums after rearranging its elements.

# https://leetcode.com/problems/maximum-alternating-sum-of-squares/

class Solution(object):
    def maxAlternatingSum(self, nums):
        return (lambda arr: sum(arr[len(nums)//2:]) - sum(arr[:len(nums)//2]))(sorted(map(lambda x:x**2, nums)))