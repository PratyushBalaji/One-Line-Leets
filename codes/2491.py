# You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. 
# Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
# The chemistry of a team is equal to the product of the skills of the players on that team.
# Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams 
#   such that the total skill of each team is equal.

# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill

class Solution(object):
    def dividePlayers(self, skill):
        return (lambda newSkill: (lambda pairings: sum(map(lambda x: x[0] * x[1], pairings)) if all(map(lambda x: x[0] + x[1] == newSkill[0] + newSkill[-1], pairings)) else -1)([[newSkill[i], newSkill[-(i+1)]] for i in range(len(skill)/2)]))(sorted(skill))