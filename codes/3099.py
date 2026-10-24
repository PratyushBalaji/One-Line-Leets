# An integer divisible by the sum of its digits is said to be a Harshad number. 
# You are given an integer x. 
# Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.

# https://leetcode.com/problems/harshad-number/

# Beats 100% in runtime and memory!
class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        return (lambda s: s if x%s == 0 else -1)(sum(map(int,list(str(x)))))
