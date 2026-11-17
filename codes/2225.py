# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
# Return a list answer of size 2 where:
#     answer[0] is a list of all players that have not lost any matches.
#     answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.
# Note:
#     You should only consider the players that have played at least one match.
#     The testcases will be generated such that no two matches will have the same outcome.

# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

# Beats 100% in memory!
class Solution(object):
    def findWinners(self, matches):
        return (lambda w, l: [sorted(w-set(l)), sorted(i for i in l if l[i] == 1)])(set(w for w,l in matches), Counter(l for w,l in matches))
