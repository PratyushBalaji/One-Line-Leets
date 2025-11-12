# One Line LeetCode Solutions

I like challenging myself to solve LeetCode problems in one single line. Code Golf : Line Edition

This game of mine started a few years ago when I would stumble upon LeetCode problems that had unsuspecting elegant solutions. Solutions that could fit in just one return statement! I wasn't intentionally seeking out solutions that consisted of a single expression, however, my interest in trying to find such one-line solutions piqued when I began learning functional programming in Racket/Scheme at the University of Waterloo, and now it's become a personal challenge of mine.

Goal : `[ "$(ls codes | wc -l)" -eq "$(grep -e "^ *return" codes/*.py | wc -l)" ] && echo "Equal" || echo "Not equal"` outputs "Equal"

---

## Rules : 
- Code must be one single line (One expression)

While `x=1; y=2; return x+y` is **technically** one line, for the spirit of the challenge it doesn't count as it is made up of three "expressions"

On the other hand, while `return max(list(map(lambda pair: pair[0] ^ pair[1], filter(lambda pair: abs(pair[0]-pair[1]) <= min(pair[0],pair[1]), list(set([(nums[i], nums[j]) for i in range(len(nums)) for j in range(i, len(nums))]))))))` is a mouthful and a half with nine consecutive closing brackets at the end, it is one single "expression". And so, it counts. (by the way, this is indeed an valid solution to [Problem #2932](https://leetcode.com/problems/maximum-strong-pair-xor-i/))

All solutions are titled by their corresponding problem number. File \<problem-number\>.py (`^[0-9]{4}.py$`) contains the problem description, a link to the problem, and my one line solution, sometimes with comments.

Disclaimer : These solutions are usually **extremely** inefficient. Sometimes they shine though.

---

## Showcase

To see a curated list of solutions that I want to showcase, including the longest, shortest, and other interesting ones, navigate to the [showcase.md](./showcase.md) file.

## Repository Contents

To see a table with all the solutions and explanations currently in the repository, navigate to the [table.md](./table.md) file.

## Compatibility

Unfortunately, while the vast majority of solutions are compatible with all major versions of Python, there are a select few that use either new or obsolete syntax and therefore are version specific. To see a list of solutions that may be dependent on a specific version of Python, navigate to the [compatibility.md](./compatibility.md) file.
