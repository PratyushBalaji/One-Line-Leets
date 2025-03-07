# You are given two integer arrays of equal length target and arr. 
# In one step, you can select any non-empty subarray of arr and reverse it. 
# You are allowed to make any number of steps.
# Return true if you can make arr equal to target or false otherwise.

# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays

class Solution(object):
    def canBeEqual(self, target, arr):
        return sorted(target) == sorted(arr)