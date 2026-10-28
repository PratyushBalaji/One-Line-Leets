# You are given a string word containing distinct lowercase English letters.
# Remap keys 2 through 9 to distinct collections of letters, with each letter
# mapped to exactly one key. Typing a letter takes as many pushes as its position
# on its key. Return the minimum number of pushes needed to type word.

# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

# Beats 100% in runtime and memory!
class Solution(object):
    def minimumPushes(self, word):
        # Actually O(1) runtime
        return (lambda l: min(8, l) + 2*min(8, max(0, l-8)) + 3*min(8, max(0, l-16)) + 4*min(8, max(0, l-24)))(len(word))

# Old : technically O(n) runtime but practically O(1) because we know len(word) <= 26
# return sum((x >> 3) for x in range(len(word))) + len(word)

# these solutions basically only work because letters are guaranteed unique and thus keypad order doesnt matter and len(word) <= 26
# if uniqueness constraint didnt exist then this is a valid one liner
# class Solution(object):
#     def minimumPushes(self, word):
#         return (lambda c: sum(((x // 8) + 1) * c[i] for x, i in enumerate(sorted(c.keys(), key=lambda y: -c[y]))))(Counter(word))
