# There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'.
# You are given a string colors of length n where colors[i] is the color of the ith piece.
# Alice and Bob are playing a game where they take alternating turns removing pieces from the line.
# In this game, Alice moves first.
#     Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'.
# She is not allowed to remove pieces that are colored 'B'.
#     Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'.
# He is not allowed to remove pieces that are colored 'A'.
#     Alice and Bob cannot remove pieces from the edge of the line.
#     If a player cannot make a move on their turn, that player loses and the other player wins.
# Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution(object):
    def winnerOfGame(self, colors):
        return False if len(colors) < 3 else (lambda r: r[0] > r[1])(reduce(lambda x,y : (lambda eq : (x[0] + (1 if eq and x[2] == 'A' else 0), x[1] + (1 if eq and x[2] == 'B' else 0), x[3], y))(x[2] == x[3] == y), colors[2:], (0, 0, colors[0], colors[1])))
