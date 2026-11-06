# A rectangular brick wall has rows of bricks of equal height and varying widths.
# The total width of each row is the same. Draw a vertical line through the wall
# crossing as few bricks as possible; passing through an internal edge crosses no brick.
# The line cannot follow either outer edge of the wall.
# Return the minimum number of crossed bricks.

# https://leetcode.com/problems/brick-wall/

# Python 3.4+: uses accumulate() and the default argument of max().
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        return (lambda edges: len(wall) - max(edges.values(), default=0))(Counter(sum((list(accumulate(i[:-1])) for i in wall), [])))

# Alternative for Python 2.7 and Python 3; recomputes prefix sums.
# class Solution(object):
#     def leastBricks(self, wall):
#         return (lambda edges: len(wall) - max([0] + list(edges.values())))(Counter(sum(([sum(row[:j]) for j in range(1, len(row))] for row in wall), [])))
