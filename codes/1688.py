# You are given an integer n, the number of teams in a tournament.
# Each round pairs teams into matches, with each winner advancing.
# If the number of teams is odd, one team advances without playing a match.
# Return the number of matches played until a winner is decided.

# https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution(object):
    def numberOfMatches(self, n):
        # Beats 100% in runtime and memory!
        return n-1

# Simulation solution :
# return sum((n>>i) + ((n>>i)&1) for i in range(1,len(str(bin(n))) -1)) - 1 + n%2
