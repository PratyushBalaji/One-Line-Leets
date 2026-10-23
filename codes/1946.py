# You are given a string num, which represents a large integer. 
# You are also given a 0-indexed integer array change of length 10 that maps each digit 0-9 to another digit. 
# More formally, digit d maps to digit change[d].
# You may choose to mutate a single substring of num. 
# To mutate a substring, replace each digit num[i] with the digit it maps to in change (i.e. replace num[i] with change[num[i]]).
# Return a string representing the largest possible integer after mutating (or choosing not to) a single substring of num.
# A substring is a contiguous sequence of characters within the string.

# https://leetcode.com/problems/largest-number-after-mutating-substring/

class Solution(object):
    def maximumNumber(self, num, change):
        return (lambda startIndex: (lambda stopIndex: num[:startIndex] + "".join(str(change[int(c)]) for c in num[startIndex:stopIndex]) + num[stopIndex:])(next((i for i, c in enumerate(num) if i > startIndex and change[int(c)] < int(c)), len(num))))(next((i for i, c in enumerate(num) if change[int(c)] > int(c)), len(num)))
