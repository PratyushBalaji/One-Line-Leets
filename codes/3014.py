# You are given a string word containing distinct lowercase English letters.
# Remap keys 2 through 9 to distinct collections of letters, with each letter
# mapped to exactly one key. Typing a letter takes as many pushes as its position
# on its key. Return the minimum number of pushes needed to type word.

# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

# Beats 100% in runtime and memory!
class Solution(object):
    def minimumPushes(self, word):
        return sum((x >> 3) for x in range(len(word))) + len(word)

# this basically only works because letters are guaranteed unique and thus order doesnt matter
# if uniqueness constraint didnt exist then this is a valid one liner
# class Solution(object):
#     def minimumPushes(self, word):
#         return (lambda c: sum(((x // 8) + 1) * c[i] for x, i in enumerate(sorted(c.keys(), key=lambda y: -c[y]))))(Counter(word))
