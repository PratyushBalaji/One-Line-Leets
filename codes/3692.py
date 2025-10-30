# You are given a string s consisting of lowercase English letters.
# The frequency group for a value k is the set of characters that appear exactly k times in s.
# The majority frequency group is the frequency group that contains the largest number of distinct characters.
# Return a string containing all characters in the majority frequency group, in any order. 
# If two or more frequency groups tie for that largest size, pick the group whose frequency k is larger.

# https://leetcode.com/problems/majority-frequency-characters/

class Solution(object):
    def majorityFrequencyGroup(self, s):
        return (lambda x: (lambda y:"".join(max(sorted([(i,y[i]) for i in y.keys()],reverse=True),key=lambda x:len(x[1]))[1])) ({i[0]:[j[1] for j in x if j[0]==i[0]] for i in x})) ([(s.count(i),i) for i in set(list(s))])