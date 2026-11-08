# You are given an integer array nums of length n and an integer k.
# For each index i, define its instability score as max(nums[0..i]) - min(nums[i..n - 1]).
# In other words:
#     max(nums[0..i]) is the largest value among the elements from index 0 to index i.
#     min(nums[i..n - 1]) is the smallest value among the elements from index i to index n - 1.
# An index i is called stable if its instability score is less than or equal to k.
# Return the smallest stable index.
# If no such index exists, return -1.

# https://leetcode.com/problems/smallest-stable-index-ii/

class Solution(object):
    def firstStableIndex(self, nums, k):
        return (lambda minnums, maxnums: next((i for i in range(len(nums)) if maxnums[i]-minnums[i] <= k), -1))(reduce(lambda a, x: (a.append(min(a[-1], x) if a else x), a)[1], reversed(nums), [])[::-1], reduce(lambda a, x: (a.append(max(a[-1], x) if a else x), a)[1], nums, []))
