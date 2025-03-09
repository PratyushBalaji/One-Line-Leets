# One Line LeetCode Solutions

I like challenging myself to solve LeetCode problems in one single line. Code Golf : Line Edition

This game of mine started a few years ago when I would stumble upon LeetCode problems that had unsuspecting elegant solutions that could fit in just one return statement. I wasn't intetionally seeking out solutions that consisted of a single expression. However, my interest in trying to find such one-line solutions piqued when I began learning functional programming in Racket/Scheme at the University of Waterloo, and now it's become a personal challenge of mine.

Goal : `[ "$(ls codes | wc -l)" -eq "$(grep -e "^ *return" codes/*.py | wc -l)" ] && echo "Equal" || echo "Not equal"` outputs "Equal"

---

## Rules : 
- Code must be one single line (One expression)

While `x=1; y=2; return x+y` is technically one line, for the spirit of the challenge this doesn't count as it is three "expressions"

However, while `return max(list(map(lambda pair: pair[0] ^ pair[1], filter(lambda pair: abs(pair[0]-pair[1]) <= min(pair[0],pair[1]), list(set([(nums[i], nums[j]) for i in range(len(nums)) for j in range(i, len(nums))]))))))` is a mouthful and a half, it is one single "expression". And so, it counts. (btw this is indeed a solution to [Problem #2932](https://leetcode.com/problems/maximum-strong-pair-xor-i/))

All solutions are titled by their corresponding problem number. File \<problem-number\>.py (`^[0-9]*.py$`) contains the problem description, a link to the problem, and my one line solution, sometimes with comments.

Disclaimer : These solutions are usually **extremely** inefficient. Sometimes they shine though.

---

## Longest and Shortest Solutions :
Metric : Convert all variable (and parameter) names to single characters, remove as much whitespace as possible, measure number of characters in the return statement (including the word `return`)

Yes, the code logic itself could be made longer (or *shorter?*) to artificially modify the result, but I'll try not to intentionally write extremely long code :P

### Shortest Solution : 
[#1025](https://leetcode.com/problems/divisor-game/) `divisorGame(self, n)` : ~~13~~ 12 Characters

Original : `return n%2==0`

~~This can even be made one character shorter in C like so :~~ `return ~n&1;` ~~. Unlike C, 0 and 1 aren't considered "boolean types" in Python, so this won't work as a Python solution. All non-zero integers are treated as True and zero, False when used in a boolean expression, but alone, they are integers. LeetCode explicitly requires a boolean returned for this question.~~

New : `return n%2<1`

### Longest Solution : 
[#2423](https://leetcode.com/problems/remove-letter-to-equalize-frequency) `equalFrequency(self, w)` : 265 Characters

`return(lambda a,b:min(a,key=a.count)==max(a,key=a.count)or min(b,key=b.count)==max(b,key=b.count))((lambda l:(lambda x:l[:l.index(x)]+l[l.index(x)+1:])(max(l,key=l.count)))(list(w)),(lambda l:(lambda x:l[:l.index(x)]+l[l.index(x)+1:])(min(l,key=l.count)))(list(w)))`

---

## Solutions I find interesting :

### Problem [#2248](https://leetcode.com/problems/intersection-of-multiple-arrays) - Intersection of Multiple Arrays
`return sorted(reduce(lambda x,y:[i for i in x if i in y],nums))`

Uses `reduce()` which works like `foldr`, accumulating results and iterating through nums to find the intersection. First solution where I tried to incorporate my (then) newly gained knowledge of the "fold" Abstract List Functions.

### Problem [#1790](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal) - Check if One String Swap Can Make Strings Equal
`return (lambda ret: False if (len(s1) != len(s2)) or (len(ret) not in {0,2}) else len(ret) == 0 or (s1[ret[0]] == s2[ret[1]] and s1[ret[1]] == s2[ret[0]]))((lambda x, y: [i for i in range(len(x)) if x[i] != y[i]])(s1, s2))`

Stacks lambda functions and assigns a larger lambda call to `ret`, using its lambda nature to avoid recomputation while keeping the solution concise. First solution where I discovered the power of using a lambda function to "store" and use variables in my One-Line-Leets

### Problem [#3226](https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal) - Number of Bit Changes to Make Two Integers Equal
Original solution : `return str(bin(n^k)).count('1') if n - (n&k) - (n^k) == k - (n&k) else 0 if n == k else -1`

Optimised solution : `return str(bin(n^k)).count('1') if n - (n^k) == k else -1`

I like this solution a lot because it uses clever bit manipulation to form an elegant, efficient solution. Let's look at why it works : 

`n&k` represents the bits in `n` and `k` that are the same. We can just ignore these bits entirely, hence they are subtracted from both. This isn't entirely necessary since we're subtracting on both sides, but when I was drawing binary numbers on my whiteboard to figure this problem out, it was immensely helpful.

Now, we're left with residuals of `n` and `k`, comprising only of the digits between them that are different. `n^k` represents the bits that are different between the two numbers. Since the question requires that we only change `1`s in `n` to `0`s and not the other way round, this must mean that if it is possible to transform `n` to `k`, subtracting the differing bits (essentially converting all ones to zeroes) should result in `k` itself! That's why we check if `n - n^k == k`!

If this is true (we *can* transform `n` into `k`), then the number of bits we changed is the number of ones in the differing bits, so we do `str(bin(n^k)).count('1')`. If there are no differing bits, we return `0`. If both of these cases are not true, then it is not possible to convert `n` to `k`, hence we return `-1`

In actuality, the solution can be made much simpler in two ways. By removing the redundant subtractions of `n&k` on both sides, and the unecessary check to see if the values are equal (`...count('1')` would return 0 in this case anyways). This results in `return str(bin(n^k)).count('1') if n - (n^k) == k else -1`, which ends up beating 100% of submissions in both runtime (0ms) and memory (12.30MB) according to LeetCode.

I love the elegance of this solution and how simple logic gates are super useful and efficient in solving this problem!

### Problem [#1752](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated) - Check if Array Is Sorted and Rotated
`return (lambda i: nums[i:] + nums[:i] == sorted(nums))((next((i for i in range(1, len(nums)) if nums[i] < nums[i-1]), 0)))`

This solution is interesting as it uses a generator expression inside `next()` to find the first index where the array starts to decrease.

It then passes said index (or 0 if none are found) into a lambda expression, which reverses a potential array rotation about this index, and checks if this reversed rotation results in a sorted array.

Alternatively, the lambda argument could've been written like so : `(([i for i in range(1, len(nums)) if nums[i] < nums[i-1]] + [0])[0])`. But this would have to traverse the whole array and find indices where it starts decreasing. The generator and `next` allow for lazy evaluation, removing the need to traverse the entire array by breaking at the first match, making the algorithm faster overall.

The latter, unoptimised approach is what I've used in the past for numerous questions (such as #3438 - Find Valid Pair of Adjacent Digits in String).

## Problems You'll Find in this Repository : 

Below is a table indicating problems I've solved and explained in one line out of all the files I've uploaded to this repository. The problem title is a link to the problem for you to try it out yourself.

Solutions can be found under `codes/` named `<problem-number>.py` and explanations under `explanations/` named `<problem-number>.md`

**Legend :**
- ✅ Complete
- ❌ Incomplete
- ⏱️ Time Limit Exceeded
- 💥 Memory Limit Exceeded

| Problem Number | Problem Title                                                                                   | Solved | Explained |
|--------|---------------------------------------------------------------------------------------------------------|--------|-----------|
| 0067   | [Add Binary](https://leetcode.com/problems/add-binary/)                                                 | ✅     | ❌       |
| 0169   | [Majority Element](https://leetcode.com/problems/majority-element/)                                     | ✅     | ❌       |
| 0190   | [Reverse Bits](https://leetcode.com/problems/reverse-bits/)                                             | ✅     | ❌       |
| 0191   | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)                                     | ✅     | ❌       |
| 0229   | [Majority Element II](https://leetcode.com/problems/majority-element-ii/)                               | ✅     | ❌       |
| 0268   | [Missing Number](https://leetcode.com/problems/missing-number/)                                         | ✅     | ❌       |
| 0338   | [Counting Bits](https://leetcode.com/problems/counting-bits/)                                           | ✅     | ❌       |
| 0372   | [Super Pow](https://leetcode.com/problems/super-pow/)                                                   | ✅     | ❌       |
| 0412   | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)                                                   | ✅     | ❌       |
| 0434   | [Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/)         | ✅     | ❌       |
| 0476   | [Number Complement](https://leetcode.com/problems/number-complement/)                                   | ✅     | ❌       |
| 0551   | [Student Attendance Record I](https://leetcode.com/problems/student-attendance-record-i/)               | ✅     | ❌       |
| 0575   | [Distribute Candies](https://leetcode.com/problems/distribute-candies/)                                 | ✅     | ❌       |
| 0648   | [Replace Words](https://leetcode.com/problems/replace-words/)                                           | ✅     | ❌       |
| 0680   | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)                               | ✅     | ❌       |
| 0693   | [Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits/) | ✅     | ❌        |
| 0821   | [Shortest Distance to a Character](https://leetcode.com/problems/shortest-distance-to-a-character/)     | ✅     | ❌       |
| 0898   | [Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays/)                     | ⏱️     | ❌       |
| 0922   | [Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/)                       | ✅     | ❌       |
| 0977   | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)                   | ✅     | ❌       |
| 0989   | [Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/)             | ✅     | ❌       |
| 1009   | [Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/)           | ✅     | ❌       |
| 1025   | [Divisor Game](https://leetcode.com/problems/divisor-game/)                                             | ✅     | ❌       |
| 1266   | [Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/)     | ✅     | ❌       |
| 1295   | [Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/) | ✅     | ❌        |
| 1317   | [Convert Integer to the Sum of Two No-Zero Integers](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/) | ✅     | ❌       |
| 1365   | [How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) | ✅     | ❌       |
| 1374   | [Generate a String With Characters That Have Odd Counts](https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/) | ✅     | ❌       |
| 1460   | [Make Two Arrays Equal by Reversing Sub-arrays](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/)         | ✅     | ❌       |
| 1486   | [XOR Operation in an Array](https://leetcode.com/problems/xor-operation-in-an-array/)                   | ✅     | ❌       |
| 1704   | [Determine if String Halves Are Alike](https://leetcode.com/problems/determine-if-string-halves-are-alike/)                           | ✅     | ❌       |
| 1752   | [Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)                           | ✅     | ❌       |
| 1790   | [Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/)     | ✅     | ❌       |
| 1805   | [Number of Different Integers in a String](https://leetcode.com/problems/number-of-different-integers-in-a-string/)                   | ✅     | ✅       |
| 1812   | [Determine Color of a Chessboard Square](https://leetcode.com/problems/determine-color-of-a-chessboard-square/)                       | ✅     | ❌       |
| 1835   | [Find XOR Sum of All Pairs Bitwise AND](https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/)                         | ✅     | ❌       |
| 1876   | [Substrings of Size Three with Distinct Characters](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/) | ✅     | ❌       |
| 1952   | [Three Divisors](https://leetcode.com/problems/three-divisors/)                                         | ✅     | ❌       |
| 1980   | [Find Unique Binary String](https://leetcode.com/problems/find-unique-binary-string/)                   | ✅     | ❌       |
| 2000   | [Reverse Prefix of Word](https://leetcode.com/problems/reverse-prefix-of-word/)                         | ✅     | ❌       |
| 2006   | [Count Number of Pairs With Absolute Difference K](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/)   | ✅     | ❌       |
| 2032   | [Two Out of Three](https://leetcode.com/problems/two-out-of-three/)                                     | ✅     | ❌       |
| 2057   | [Smallest Index With Equal Value](https://leetcode.com/problems/smallest-index-with-equal-value/)       | ✅     | ❌       |
| 2089   | [Find Target Indices After Sorting Array](https://leetcode.com/problems/find-target-indices-after-sorting-array/)                     | ✅     | ❌       |
| 2108   | [Find First Palindromic String in the Array](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/)               | ✅     | ❌       |
| 2114   | [Maximum Number of Words Found in Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/)               | ✅     | ❌       |
| 2161   | [Partition Array According to Given Pivot](https://leetcode.com/problems/partition-array-according-to-given-pivot/)                   | ✅     | ❌       |
| 2185   | [Counting Words With a Given Prefix](https://leetcode.com/problems/counting-words-with-a-given-prefix/) | ✅     | ❌       |
| 2206   | [Divide Array Into Equal Pairs](https://leetcode.com/problems/divide-array-into-equal-pairs/)           | ✅     | ❌       |
| 2239   | [Find Closest Number to Zero](https://leetcode.com/problems/find-closest-number-to-zero/)               | ✅     | ❌       |
| 2248   | [Intersection of Multiple Arrays](https://leetcode.com/problems/intersection-of-multiple-arrays/)       | ✅     | ❌       |
| 2255   | [Count Prefixes of a Given String](https://leetcode.com/problems/count-prefixes-of-a-given-string/)     | ✅     | ❌       |
| 2259   | [Remove Digit From Number to Maximize Result](https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/)             | ✅     | ❌       |
| 2364   | [Count Number of Bad Pairs](https://leetcode.com/problems/count-number-of-bad-pairs/)                   | 💥     | ❌       |
| 2418   | [Sort the People](https://leetcode.com/problems/sort-the-people/)                                       | ✅     | ❌       |
| 2423   | [Remove Letter To Equalize Frequency](https://leetcode.com/problems/remove-letter-to-equalize-frequency/)                             | ✅     | ❌       |
| 2455   | [Average Value of Even Numbers That Are Divisible by Three](https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/) | ✅     | ❌        |
| 2491   | [Divide Players Into Teams of Equal Skill](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/)                   | ✅     | ❌       |
| 2535   | [Difference Between Element Sum and Digit Sum of an Array](https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/) | ✅     | ❌        |
| 2549   | [Count Distinct Numbers on Board](https://leetcode.com/problems/count-distinct-numbers-on-board/)       | ✅     | ❌       |
| 2553   | [Separate the Digits in an Array](https://leetcode.com/problems/separate-the-digits-in-an-array/)       | ✅     | ❌       |
| 2570   | [Merge Two 2D Arrays by Summing Values](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/)                         | ✅     | ❌       |
| 2579   | [Count Total Number of Colored Cells](https://leetcode.com/problems/count-total-number-of-colored-cells/)                             | ✅     | ❌       |
| 2651   | [Calculate Delayed Arrival Time](https://leetcode.com/problems/calculate-delayed-arrival-time/)         | ✅     | ❌       |
| 2652   | [Sum Multiples](https://leetcode.com/problems/sum-multiples/)                                           | ✅     | ❌       |
| 2656   | [Maximum Sum With Exactly K Elements](https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/)                             | ✅     | ❌       |
| 2678   | [Number of Senior Citizens](https://leetcode.com/problems/number-of-senior-citizens/)                   | ✅     | ❌       |
| 2710   | [Remove Trailing Zeros From a String](https://leetcode.com/problems/remove-trailing-zeros-from-a-string/)                             | ✅     | ❌       |
| 2716   | [Minimize String Length](https://leetcode.com/problems/minimize-string-length/)                         | ✅     | ❌       |
| 2788   | [Split Strings by Separator](https://leetcode.com/problems/split-strings-by-separator/)                 | ✅     | ❌       |
| 2798   | [Number of Employees Who Met the Target](https://leetcode.com/problems/number-of-employees-who-met-the-target/)                       | ✅     | ❌       |
| 2828   | [Check if a String Is an Acronym of Words](https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/)                   | ✅     | ❌       |
| 2864   | [Maximum Odd Binary Number](https://leetcode.com/problems/maximum-odd-binary-number/)                   | ✅     | ❌       |
| 2932   | [Number of Employees Who Met the Target](https://leetcode.com/problems/number-of-employees-who-met-the-target/)                       | ✅     | ❌       |
| 2980   | [Check if Bitwise OR has Trailing Zeros](https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/)                       | ✅     | ❌       |
| 3019   | [Number of Changing Keys](https://leetcode.com/problems/number-of-changing-keys/)                       | ✅     | ❌       |
| 3042   | [Count Prefix and Suffix Pairs I](https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/)       | ✅     | ❌       |
| 3079   | [Find the Sum of Encrypted Integers](https://leetcode.com/problems/find-the-sum-of-encrypted-integers/) | ✅     | ❌       |
| 3083   | [Existence of a Substring in a String and its Reverse](https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/) | ✅     | ❌       |
| 3110   | [Score of a String](https://leetcode.com/problems/score-of-a-string/)                                   | ✅     | ❌       |
| 3136   | [Valid Word](https://leetcode.com/problems/valid-word)                                                  | ✅     | ❌       |
| 3151   | [Special Array I](https://leetcode.com/problems/special-array-i/)                                       | ✅     | ❌       |
| 3226   | [Number of Bit Changes to Make Two Integers Equal](https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/)   | ✅     | ❌       |
| 3340   | [Check Balanced String](https://leetcode.com/problems/check-balanced-string/)                           | ✅     | ❌       |
| 3438   | [Find Valid Pair of Adjacent Digits in String](https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/)                  | ✅     | ❌        |
| 3442   | [Maximum Difference Between Even and Odd Frequency](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/)                  | ✅     | ❌        |