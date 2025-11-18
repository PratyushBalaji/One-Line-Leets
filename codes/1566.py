# Given an array of positive integers arr, find a pattern of length m that is repeated k or more times.
# A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. 
# A pattern is defined by its length and the number of repetitions.
# Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.

# https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

# Beats 100% in runtime and memory!
class Solution(object):
    def containsPattern(self, arr, m, k):
        return next((True for i in range(m) for j in range(i,len(arr)-(k*m)+1,m) if arr[j:j+m]*k == arr[j:j+(m*k)]),False)