# Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.
# Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer. 

# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three

class Solution(object):
    def averageValue(self, nums):
        return (lambda lst:int(sum(lst)/len(lst)) if lst else 0) (filter(lambda x: not (x%3 or x%2),nums))