# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

# Requires Python 3.8+

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        return max((lambda first: [first] + [first := (first - cardPoints[k - i - 1] + cardPoints[-(i + 1)]) for i in range(k)])(sum(cardPoints[:k])))