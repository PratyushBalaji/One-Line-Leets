# You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:
# |x - y| <= min(x, y)
# You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.
# Return the maximum XOR value out of all possible strong pairs in the array nums.
# Note that you can pick the same integer twice to form a pair.

# https://leetcode.com/problems/maximum-strong-pair-xor-i/

class Solution(object):
    def maximumStrongPairXor(self, nums):
        return max(list(map(lambda pair: pair[0] ^ pair[1], filter(lambda pair: abs(pair[0]-pair[1]) <= min(pair[0],pair[1]), list(set([(nums[i], nums[j]) for i in range(len(nums)) for j in range(i, len(nums))]))))))