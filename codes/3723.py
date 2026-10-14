# You are given two positive integers num and sum.
# A positive integer n is good if it satisfies both of the following:
#     The number of digits in n is exactly num.
#     The sum of digits in n is exactly sum.
# The score of a good integer n is the sum of the squares of digits in n.
# Return a string denoting the good integer n that achieves the maximum score. 
# If there are multiple possible integers, return the maximum ​​​​​​​one. 
# If no such integer exists, return an empty string.

# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

class Solution(object):
    def maxSumOfSquares(self, n, s):
        return "" if s > 9*n else ''.join(map(str, [(9 if s-(9*i) > 9 else max(0,s-(9*i))) for i in range(n)]))

# uses same construction as problem 4000
# since (a+b)^2 > a^2 + b^2, the maximum score will be for the number with the largest digits which is maximally contructed in 4000
