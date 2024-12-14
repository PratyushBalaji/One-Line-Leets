# You are given a positive integer n, that is initially placed on a board. Every day, for 109 days, you perform the following procedure:
#     For each number x present on the board, find all numbers 1 <= i <= n such that x % i == 1.
#     Then, place those numbers on the board.
# Return the number of distinct integers present on the board after 109 days have elapsed.

# https://leetcode.com/problems/count-distinct-numbers-on-board/

class Solution(object):
    def distinctIntegers(self, n):
        return 1 if n == 1 else n-1