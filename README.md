# One Line LeetCode Solutions

I like challenging myself to solve LeetCode problems in one single line. Code Golf : Line Edition

---

## Rules : 
- Code must be one single line (One expression)

While `x=1; y=2; return x+y` is technically one line, for the spirit of the competition this doesn't count as it is three expressions

However, while `return max(list(map(lambda pair: pair[0] ^ pair[1], filter(lambda pair: abs(pair[0]-pair[1]) <= min(pair[0],pair[1]), list(set([(nums[i], nums[j]) for i in range(len(nums)) for j in range(i, len(nums))]))))))` is a mouthful and a half, it is one single expression and so it counts. (btw this is a solution to [Problem #2932](https://leetcode.com/problems/maximum-strong-pair-xor-i/))

All solutions are titled by their corresponding problem number. File contains the problem description, a link to the problem, and the code

Disclaimer : These solutions are usually **extremely** inefficient. Sometimes they shine though.

---

## Solutions I find interesting :

### Problem [#2248](https://leetcode.com/problems/intersection-of-multiple-arrays) - Intersection of Multiple Arrays
`return sorted(reduce(lambda x,y:[i for i in x if i in y],nums))`

Uses `reduce()` which works like `foldr`, accumulating results and iterating through nums to find the intersection. First solution where I tried to incorporate my (then) newly gained knowledge of the "fold" Abstract List Functions.

### Problem [#1790](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal) - Check if One String Swap Can Make Strings Equal
`return (lambda ret: False if (len(s1) != len(s2)) or (len(ret) not in {0,2}) else len(ret) == 0 or (s1[ret[0]] == s2[ret[1]] and s1[ret[1]] == s2[ret[0]]))((lambda x, y: [i for i in range(len(x)) if x[i] != y[i]])(s1, s2))`

Stacks lambda functions and assigns a larger lambda call to `ret`, using its lambda nature to avoid recomputation while keeping the solution concise. First solution where I discovered the power of using a lambda function to "store" and use variables in my One-Line-Leets
