# Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

# https://leetcode.com/problems/super-pow/

class Solution(object):
    def superPow(self, a, b):
        return pow(a,int("".join([str(i) for i in b])),1337)