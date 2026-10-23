# You are given an integer n.
# Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.
# In standard formatting:
#     A comma is inserted after every three digits from the right.
#     Numbers with fewer than 4 digits contain no commas.

# https://leetcode.com/problems/count-commas-in-range/

class Solution(object):
    def countCommas(self, n):
        return max(0,n-999)
        # works because top constrain is 10**5, it it was >= 10**7 will need to account for 2 comma numbers
