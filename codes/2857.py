# You are given a 2D integer array coordinates and an integer k, where coordinates[i] = [xi, yi] are the coordinates of the ith point in a 2D plane.
# We define the distance between two points (x1, y1) and (x2, y2) as (x1 XOR x2) + (y1 XOR y2) where XOR is the bitwise XOR operation.
# Return the number of pairs (i, j) such that i < j and the distance between points i and j is equal to k.

# https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

class Solution(object):
    def countPairs(self, coordinates, k):
        # Beats 100% in memory!
        return (lambda c: sum(n*(n-1)/2 for n in c.values()) if k == 0 else sum(c[(x1,y1)]*c[(i^x1, (k-i)^y1)] for i in range(k+1) for x1, y1 in c.keys() if (i^x1, (k-i)^y1) in c)//2)(Counter(map(tuple, coordinates)))
