# You are given an array of strings words and an integer k.
# Two words a and b at distinct indices are prefix-connected if a[0..k-1] == b[0..k-1].
# A connected group is a set of words such that each pair of words is prefix-connected.
# Return the number of connected groups that contain at least two words, formed from the given words.
# Note:
#     Words with length less than k cannot join any group and are ignored.
#     Duplicate strings are treated as separate words.

# https://leetcode.com/problems/number-of-prefix-connected-groups/

class Solution(object):
    def prefixConnected(self, words, k):
        return (lambda c: sum(1 for i in c.keys() if c[i] >= 2))(Counter([i[:k] for i in words if len(i) >= k]))
