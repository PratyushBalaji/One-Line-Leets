# Given points on the X-Y plane and an integer k, return the k closest points
# to the origin (0, 0) by Euclidean distance. The answer is unique except for
# its order, and the points may be returned in any order.

# https://leetcode.com/problems/k-closest-points-to-origin/

# Beats 100% in runtime and memory!
class Solution(object):
    def kClosest(self, points, k):
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]
