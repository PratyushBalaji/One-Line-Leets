# You are given a positive integer n. Its most significant digit has a positive
# sign, and each subsequent digit has the opposite sign to its adjacent digits.
# Return the sum of all digits with their corresponding sign.

# https://leetcode.com/problems/alternating-digit-sum/

# Beats 100% in runtime!
class Solution(object):
    def alternateDigitSum(self, n):
        return sum(int(i)*(1-((x%2)*2)) for x, i in enumerate(str(n)))
