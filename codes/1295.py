# Given an array nums of integers, return how many of them contain an even number of digits.

# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution(object):
    def findNumbers(self, nums):
        return len(filter(lambda x:len(x)%2==0,map(str,nums)))