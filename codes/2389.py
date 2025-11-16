# You are given an integer array nums of length n, and an integer array queries of length m.
# Return an array answer of length m where answer[i] is the maximum size of a subsequence 
# that you can take from nums such that the sum of its elements is less than or equal to queries[i].
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

# https://leetcode.com/problems/longest-subsequence-with-limited-sum/

class Solution(object):
    def answerQueries(self, nums, queries):
        return (lambda dct: [dct.get(max([j for j in dct.keys() if j <= i]),0) for i in queries])((lambda sortedNums: {sum(sortedNums[:i]):i for i in range(len(nums)+1)})(sorted(nums)))