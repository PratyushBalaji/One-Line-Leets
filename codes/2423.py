# You are given a 0-indexed string word, consisting of lowercase English letters. 
# You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.
# Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.
# Note:
#     The frequency of a letter x is the number of times it occurs in the string.
#     You must remove exactly one letter and cannot choose to do nothing.

# https://leetcode.com/problems/remove-letter-to-equalize-frequency

class Solution(object):
    def equalFrequency(self, bird):
        return (lambda w1, w2: min(w1, key=w1.count) == max(w1, key=w1.count) or min(w2, key=w2.count) == max(w2, key=w2.count))((lambda lst: (lambda x: lst[:lst.index(x)] + lst[lst.index(x)+1:])(max(lst, key=lst.count)))(list(bird)),(lambda lst: (lambda x: lst[:lst.index(x)] + lst[lst.index(x)+1:])(min(lst, key=lst.count)))(list(bird)))