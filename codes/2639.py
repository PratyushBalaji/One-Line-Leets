# You are given a 0-indexed m x n integer matrix grid. The width of a column is the maximum length of its integers.
#     For example, if grid = [[-10], [3], [12]], the width of the only column is 3 since -10 is of length 3.
# Return an integer array ans of size n where ans[i] is the width of the ith column.
# The length of an integer x with len digits is equal to len if x is non-negative, and len + 1 otherwise.

# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution(object):
    def findColumnWidth(self, grid):
        return [len(max(x,key=len)) for x in map(lambda x: map(str,x), [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))])]