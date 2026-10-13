# You are given an m x n binary matrix matrix.
# You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).
# Return the maximum number of rows that have all values equal after some number of flips.

# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

# Beats 100% in memory!
class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        return max(Counter(map(lambda row: "".join([str(i) if row[0] == 0 else str(1-i) for i in row]), matrix)).values())
