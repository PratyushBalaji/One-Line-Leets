# You are given a binary array nums (0-indexed).
# We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).
#     For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
# Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

# https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution(object):
    def prefixesDivBy5(self, nums):
        return (lambda strnums: [int("".join(strnums[:i+1]),2) % 5 == 0 for i in range(len(nums))])(map(str,nums))