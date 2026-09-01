# You are given two integers n and k.
# A positive integer x is called compatible if it satisfies both of the following conditions:
#     abs(n - x) <= k
#     (n & x) == 0
# Return the sum of all compatible integers x.
# Note:
#     Here, & denotes the bitwise AND operator.
#     The absolute difference between integers i and j is defined as abs(i - j).

# https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/

# Beats 100% in runtime
class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        return sum((x for x in range(max(1,n-k),n+k+1) if (n&x)==0))
