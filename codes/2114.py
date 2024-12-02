# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
# Return the maximum number of words that appear in a single sentence.

# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution(object):
    def mostWordsFound(self, sentences):
        return max([i.count(' ')+1 for i in sentences]+[0])