# You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [0..n - 1].
# You may swap elements at indices i and j only if nums[i] AND nums[j] == k, where AND denotes the bitwise AND operation and k is a non-negative integer.
# Return the maximum value of k such that the array can be sorted in non-decreasing order using any number of such swaps. 
# If nums is already sorted, return 0.

# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

class Solution(object):
    def sortPermutation(self, nums):
        return max(reduce(lambda x,y : x&y, [i for x, i in enumerate(nums) if i != x], -1), 0)
        
# Old : 
# return (lambda s: (lambda lst: reduce(lambda x,y : x&y, lst) if lst else 0)([i for x, i in enumerate(nums) if i != s[x]]))(sorted(nums))

# Better : 
# return (lambda lst: reduce(lambda x,y : x&y, lst) if lst else 0)([i for x, i in enumerate(nums) if i != x])
