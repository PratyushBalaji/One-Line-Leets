# Given an array nums of positive integers, an operation deletes either two
# or three elements with equal values. Return the minimum number of operations
# needed to empty the array, or -1 if it is impossible.

# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

class Solution(object):
    def minOperations(self, nums):
        return (lambda c: -1 if 1 in c else sum(i//3 if i%3==0 else 2+(i-4)//3 if i%3==1 else 1+(i-2)//3 for i in c))(Counter(nums).values())
