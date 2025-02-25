# You are given two positive integers n and k.
# You can choose any bit in the binary representation of n that is equal to 1 and change it to 0.
# Return the number of changes needed to make n equal to k. If it is impossible, return -1.

# https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal

class Solution(object):
    def minChanges(self, n, k):
        return str(bin(n^k)).count('1') if n - (n&k) - (n^k) == k - (n&k) else 0 if n == k else -1