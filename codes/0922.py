# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.

# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution(object):
    def sortArrayByParityII(self, nums):
        return (lambda evens,odds:reduce(lambda x,y: x + y,[[evens[i],odds[i]] for i in range(len(evens))]))(filter(lambda x:x%2==0,nums),filter(lambda x:x%2==1,nums))