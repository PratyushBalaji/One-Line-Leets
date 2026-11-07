# Given an integer array arr, return whether it is a valid mountain array.
# A mountain has at least three elements, strictly increases to an interior peak,
# then strictly decreases through the last element.

# https://leetcode.com/problems/valid-mountain-array/

# Beats 100% in memory!
class Solution(object):
    def validMountainArray(self, arr):
        return (lambda f: False if len(arr) < 3 or f < 2 or arr[f] == arr[f-1] else next((i for i in range(f, len(arr)) if arr[i] >= arr[i-1]), -1) == -1)(next((i for i in range(1, len(arr)) if arr[i] <= arr[i-1]), -1))
