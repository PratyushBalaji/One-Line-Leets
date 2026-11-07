# You are given a string moves consisting of 'L', 'R', and '_', describing moves
# on a number line starting at 0. 'L' moves left, 'R' moves right, and '_' may
# move in either direction. Return the furthest distance from the origin possible.

# https://leetcode.com/problems/furthest-point-from-origin/

# Beats 100% in runtime and memory!
class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        return abs(moves.count('R') - moves.count('L')) + moves.count('_')
