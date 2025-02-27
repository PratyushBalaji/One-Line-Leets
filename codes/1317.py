# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.
# Given an integer n, return a list of two integers [a, b] where:
#     a and b are No-Zero integers.
#     a + b = n
# The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers

class Solution(object):
    def getNoZeroIntegers(self, n):
        return filter(lambda x: '0' not in str(x[0]) and '0' not in str(x[1]), list([[a,n-a] for a in range(n)]))[0]