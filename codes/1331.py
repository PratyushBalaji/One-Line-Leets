# Given an array of integers arr, replace each element with its rank.
# The rank represents how large the element is. The rank has the following rules:
#     Rank is an integer starting from 1.
#     The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
#     Rank should be as small as possible.

# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution(object):
    def arrayRankTransform(self, arr):
        return (lambda dct: [dct[i] for i in arr])((lambda newarr: {i:j for i,j in newarr})(zip(sorted(list(set(arr))),range(1,1+len(set(arr))))))