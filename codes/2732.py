# You are given a 0-indexed m x n binary matrix grid.
# A non-empty subset of k rows is good if each column's sum is at most floor(k / 2).
# Return the row indices of any good subset in ascending order, or an empty array
# if no good subset exists. A subset is formed by deleting some or no rows.

# https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

# Beats 100% in memory!
# Python 2: dict.keys() and dict.values() return indexable lists.
class Solution(object):
    def goodSubsetofBinaryMatrix(self, grid):
        return (lambda dct: next((sorted([dct.values()[i], dct.values()[j]]) for i in range(len(dct)-1) for j in range(i+1, len(dct)) if dct.keys()[i] & dct.keys()[j] == 0), [0] if dct.keys()[0] == 0 else []))({sum(i << x for x, i in enumerate(j[::-1])) : y for y, j in enumerate(grid)})
