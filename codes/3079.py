# You are given an integer array nums containing positive integers. 
# We define a function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x. 
# For example, encrypt(523) = 555 and encrypt(213) = 333.
# Return the sum of encrypted elements.

# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

class Solution(object):
    def sumOfEncryptedInt(self, nums):
        return sum(list(map(lambda num: int(len(str(num)) * max([i for i in str(num)], key=ord)), nums)))
    
# Beats 98.10% in Runtime!