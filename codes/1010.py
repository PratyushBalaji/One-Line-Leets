# You are given a list of songs where the ith song has a duration of time[i] seconds.
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
# Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        return (lambda c: sum(c[i]*c[60-i] for i in range(1,30)) + (c[0]*(c[0]-1))//2 + (c[30]*(c[30]-1))//2)(Counter(map(lambda x: x%60, time)))
