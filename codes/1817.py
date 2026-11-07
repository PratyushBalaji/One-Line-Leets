# Given logs of actions [user ID, minute], a user's active minutes (UAM) is the
# number of unique minutes in which they performed an action. Repeated actions
# in the same minute count only once.
# Return an array of length k whose jth entry counts users with UAM equal to j,
# where j is 1-indexed.

# https://leetcode.com/problems/finding-the-users-active-minutes/

class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        return (lambda c: [c[i] for i in range(1, k+1)])(Counter(map(len, reduce(lambda d, p: (d.setdefault(p[0], set()).add(p[1]), d)[1], logs, {}).values())))
