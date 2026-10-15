# You are given two integer arrays x and y, each of length n. 
# You must choose three distinct indices i, j, and k such that:
#     x[i] != x[j]
#     x[j] != x[k]
#     x[k] != x[i]
# Your goal is to maximize the value of y[i] + y[j] + y[k] under these conditions. 
# Return the maximum possible sum that can be obtained by choosing such a triplet of indices.
# If no such triplet exists, return -1.

# https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

class Solution(object):
    def maxSumDistinctTriplet(self, x, y):
        return (lambda szd: -1 if len(szd) < 3 else sum(sorted(szd.values(),reverse=True)[:3]))({i:j for i,j in sorted(zip(x,y))})
