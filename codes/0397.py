# Given a positive integer n, you can apply one of the following operations:
#     If n is even, replace n with n / 2.
#     If n is odd, replace n with either n + 1 or n - 1.
# Return the minimum number of operations needed for n to become 1.

# https://leetcode.com/problems/integer-replacement/

# Beats 100% in runtime and memory!
class Solution(object):
    def integerReplacement(self, n):
        return (lambda a: reduce(lambda x,y: x if y == 1 else (a.append((y//2 if y%2 == 0 else y-1 if y==3 or y%4==1 else y+1)), x+1)[1], a, 0))([n])
