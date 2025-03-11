# There exists an infinitely large two-dimensional grid of uncolored unit cells. 
# You are given a positive integer n, indicating that you must do the following routine for n minutes:
#     At the first minute, color any arbitrary unit cell blue.
#     Every minute thereafter, color blue every uncolored cell that touches a blue cell.
# Return the number of colored cells at the end of n minutes.

# https://leetcode.com/problems/count-total-number-of-colored-cells

class Solution(object):
    def coloredCells(self, n):
        return (n)*(n-1)*2 + 1