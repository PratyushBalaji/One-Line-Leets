# Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.
# Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

# https://leetcode.com/problems/sum-multiples/

class Solution(object):
    def sumOfMultiples(self, n):
        return sum(filter(lambda x: x%3 == 0 or x%5 == 0 or x%7 == 0,range(1,n+1)))