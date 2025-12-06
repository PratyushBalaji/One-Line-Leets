# You are given a string s. Simulate events at each second i:
#     If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
#     If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
# Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially empty.

# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

class Solution:
    def minimumChairs(self, s: str) -> int:
        return max(accumulate(map(lambda x: 1 if x=='E' else -1, s)))