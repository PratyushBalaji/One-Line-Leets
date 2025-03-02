# Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.
# The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. 
# The bitwise OR of a subarray of one integer is that integer.
# A subarray is a contiguous non-empty sequence of elements within an array.

# https://leetcode.com/problems/bitwise-ors-of-subarrays

class Solution(object):
    def subarrayBitwiseORs(self, arr):
        return len(set([reduce(lambda x,y:x|y,a) for a in [arr[j:j+i] for i in range(1,len(arr)+1) for j in range(len(arr)-i+1)]]))
    
# works in theory but TLE in practice