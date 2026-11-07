# There are n cities numbered from 0 to n - 1 and bidirectional roads connecting them.
# Assign each city a unique value from 1 to n. A road's importance is the sum of
# its endpoints' values. Return the maximum total importance of all roads.

# https://leetcode.com/problems/maximum-total-importance-of-roads/

class Solution(object):
    def maximumImportance(self, n, roads):
        return (lambda c: sum((n-x)*c[i] for x, i in enumerate(sorted(c.keys(), key=c.get, reverse=True))))(dict(Counter([r[0] for r in roads]) + Counter([r[1] for r in roads])))
