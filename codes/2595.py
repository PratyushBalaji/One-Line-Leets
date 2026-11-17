# You are given a positive integer n.
# Let even denote the number of even indices in the binary representation of n with value 1.
# Let odd denote the number of odd indices in the binary representation of n with value 1.
# Note that bits are indexed from right to left in the binary representation of a number.
# Return the array [even, odd].

# https://leetcode.com/problems/number-of-even-and-odd-bits/

# Beats 100% in memory!
class Solution(object):
    def evenOddBit(self, n):
        return reduce(lambda x, y: [x[0]+(1-(y&1)), x[1]+(y&1)] if n&(1<<y) else x, range(n.bit_length()), [0,0])
