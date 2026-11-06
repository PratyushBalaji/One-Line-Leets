# Given an integer number n, return the difference between the product of its
# digits and the sum of its digits.

# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

# Beats 100% in memory!
class Solution(object):
    def subtractProductAndSum(self, n):
        return int(reduce(lambda x,y: str(int(x)*int(y)), str(n))) - int(reduce(lambda x,y: str(int(x)+int(y)), str(n)))
