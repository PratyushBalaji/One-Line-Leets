# Given 2 integers n and start. Your task is return any permutation p of (0,1,2.....,2^n -1) such that :
#     p[0] = start
#     p[i] and p[i+1] differ by only one bit in their binary representation.
#     p[0] and p[2^n -1] must also differ by only one bit in their binary representation.

# https://leetcode.com/problems/circular-permutation-in-binary-representation/

# Beats 100% in runtime!
# Graycode is problem #89 so this solution uses that valid graycode array and rotates it to begin at start
class Solution(object):
    def circularPermutation(self, n, start):
        return (lambda grayCode: grayCode[grayCode.index(start):]+grayCode[:grayCode.index(start)])([i^(i>>1) for i in range(1<<n)])