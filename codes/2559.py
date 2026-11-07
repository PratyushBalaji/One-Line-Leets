# You are given a 0-indexed array of strings words and an array of queries.
# Each query [l, r] asks how many words from index l through r, inclusive,
# start and end with a vowel. Return the answer for each query.
# The vowels are 'a', 'e', 'i', 'o', and 'u'.

# https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        return (lambda pref: [pref[r+1]-pref[l] for l,r in queries])([0] + list(accumulate([1 if len({'a','e','i','o','u',w[0],w[-1]}) == 5 else 0 for w in words])))
