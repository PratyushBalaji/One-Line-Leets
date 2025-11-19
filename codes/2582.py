# There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. 
# Every second, the person holding the pillow passes it to the next person standing in the line.
# Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.
#     For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
# Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.

# https://leetcode.com/problems/pass-the-pillow/

# Beats 100% in runtime!
class Solution(object):
    def passThePillow(self, n, time):
        return (lambda newtime: n - (newtime - n) - 1 if newtime >= n else 1 + newtime)(time % (2*(n-1)))