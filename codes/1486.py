# You are given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

# https://leetcode.com/problems/xor-operation-in-an-array

class Solution(object):
    def xorOperation(self, n, start):
        return reduce(lambda x,y:x^y,[start + 2*i for i in range(n)])