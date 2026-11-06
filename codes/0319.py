# There are n bulbs that are initially off. On round i, toggle every ith bulb.
# Return the number of bulbs that are on after n rounds.

# https://leetcode.com/problems/bulb-switcher/description/

# Beats 100% in runtime and memory!
class Solution(object):
    def bulbSwitch(self, n):
        return int(n**0.5)
