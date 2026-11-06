# Given a square matrix mat, return the sum of the matrix diagonals.
# Include all primary diagonal elements and only secondary diagonal elements
# that are not part of the primary diagonal.

# https://leetcode.com/problems/matrix-diagonal-sum/

# Beats 100% in memory!
class Solution(object):
    def diagonalSum(self, mat):
        return sum(mat[i][i] + mat[i][len(mat)-i-1] for i in range(len(mat))) - (0 if len(mat)% 2 == 0 else mat[len(mat)//2][len(mat)//2])
