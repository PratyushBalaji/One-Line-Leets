# You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.
#     For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the keys "name" and "age".
# You know the values of a wide range of keys.
# This is represented by a 2D string array knowledge where each knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.
# You are tasked to evaluate all of the bracket pairs.
# When you evaluate a bracket pair that contains some key keyi, you will:
#     Replace keyi and the bracket pair with the key's corresponding valuei.
#     If you do not know the value of the key, you will replace keyi and the bracket pair with a question mark "?" (without the quotation marks).
# Each key will appear at most once in your knowledge.
# There will not be any nested brackets in s.
# Return the resulting string after evaluating all of the bracket pairs.

# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

# Beats 100% in memory!
class Solution(object):
    def evaluate(self, s, knowledge):
        return (lambda d: reduce(lambda x,y: (x[0], x[1], True) if y == '(' else (x[0] + d.get(x[1],"?"), "", False) if y == ')' else (x[0] + (y if not x[2] else ""), x[1] + (y if x[2] else ""), x[2]), s, ("","",False))[0])({k:v for k,v in knowledge})
