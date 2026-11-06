# You are given an integer array nums. Return the sign of the product of its values:
# 1 if positive, -1 if negative, or 0 if the product is zero.

# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

# Beats 100% in runtime!
class Solution(object):
    def arraySign(self, nums):
        return 0 if 0 in nums else 1 - (len([i for i in nums if i < 0]) % 2)*2
