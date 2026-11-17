# You are given a positive integer n.
# Return the maximum product of any two digits in n.
# Note: You may use the same digit twice if it appears more than once in n.

# https://leetcode.com/problems/maximum-product-of-two-digits/

class Solution(object):
    def maxProduct(self, n):
        return (lambda s: int(s[0])*int(s[1]))(sorted(list(str(n)), reverse=True))
