# Given a 0-indexed 1-dimensional array, and two integers m and n, 
# create a 2-dimensional (2D) array with m rows and n columns using all the elements from original.

# The elements 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, 
# the elements n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

# Return an mxn 2D array constructed according to the above procedure,
# or an empty 2D array if it is impossible.

# https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution(object):
    def construct2DArray(self, original, m, n):
        return [] if m*n != len(original) else [original[i*n:n+(i*n)] for i in range(m)]