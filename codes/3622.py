# You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:
#     The digit sum of n (the sum of its digits).
#     The digit product of n (the product of its digits).
# Return true if n is divisible by this sum; otherwise, return false.

# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

# Beats 100% in runtime
class Solution(object):
    def checkDivisibility(self, n):
        return (n % ((reduce(lambda x,y:x+y,map(int,list(str(n))),0)) + (reduce(lambda x,y:x*y,map(int,list(str(n))),1)))) == 0