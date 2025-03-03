# You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
# Return the total number of bad pairs in nums.

# https://leetcode.com/problems/count-number-of-bad-pairs/description

class Solution(object):
    def countBadPairs(self, nums):
        return len(filter(lambda pair:pair[1]-pair[0] != nums[pair[1]]-nums[pair[0]],[(i,j) for i in range(len(nums)) for j in range(i+1,len(nums))]))
    
# Works in theory but MLE in practice