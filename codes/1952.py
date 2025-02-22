# Given an integer n, return true if n has exactly three positive divisors. 
# Otherwise, return false.
# An integer m is a divisor of n if there exists an integer k such that n = k * m.

# https://leetcode.com/problems/three-divisors

class Solution(object):
    def isThree(self, n):
        return (lambda root: root == int(root) and (lambda num: all([(num%j) for j in range(2, int(num**0.5) + 1)]) and num > 1)(root))(n**0.5)