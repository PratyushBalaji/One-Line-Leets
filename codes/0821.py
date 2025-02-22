# Given a string s and a character c that occurs in s, 
# return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

# https://leetcode.com/problems/shortest-distance-to-a-character

class Solution(object):
    def shortestToChar(self, s, c):
        return (lambda indices:list(map(lambda x: min([abs(x-i) for i in indices]),range(len(s)))))([i for i in range(len(s)) if s[i] == c])