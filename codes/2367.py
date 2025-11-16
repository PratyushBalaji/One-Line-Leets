# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. 
# A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
#     i < j < k,
#     nums[j] - nums[i] == diff, and
#     nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

# https://leetcode.com/problems/number-of-arithmetic-triplets/

class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        return sum(1 for i in range(len(nums)-2) for j in range(i+1,len(nums)-1) for k in range(j+1,len(nums)) if nums[j] - nums[i] == nums[k] - nums[j] == diff)