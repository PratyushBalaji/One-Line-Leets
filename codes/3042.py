# You are given a 0-indexed string array words.
# Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
#     isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.
# For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.
# Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i

class Solution(object):
    def countPrefixSuffixPairs(self, words):
        return len(filter(lambda tup: (lambda fix, word: word.startswith(fix) and word[::-1].startswith(fix[::-1]))(tup[0], tup[1]),[(words[i],words[j]) for i in range(len(words)) for j in range(i+1,len(words))]))