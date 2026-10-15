# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c)
  # - that is, one domino can be rotated to be equal to another domino.
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        return sum(map(lambda x: (x * (x - 1) // 2), Counter([(i[0],i[1]) if i[0] > i[1] else (i[1],i[0]) for i in dominoes]).values()))
