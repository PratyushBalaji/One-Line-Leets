# You are given a 2D integer array tasks where tasks[i] = [s_i, t_i].
# Each [s_i, t_i] in tasks represents a task with start time s_i that takes t_i units of time to finish.
# Return the earliest time at which at least one task is finished.

# https://leetcode.com/problems/earliest-time-to-finish-one-task/

class Solution(object):
    def earliestTime(self, tasks):
        return min(t[0]+t[1] for t in tasks)