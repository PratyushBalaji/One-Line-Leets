# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. 
# For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".
# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. 
# If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.
# Return the sentence after the replacement.

# https://leetcode.com/problems/replace-words

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        return (lambda newDict: ' '.join(map(lambda word:([i for i in newDict if word.startswith(i)] + [word])[0], sentence.split(' '))))(sorted(dictionary,key=len))