class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]

'''
Can the first i characters of s be segmented?

If the prefix s[:i] is segmentable, then there must be a last word in that segmentation.


Outer loop (i): picks the end position we're currently deciding. "Is dp[i] True? Can the first i characters be segmented?"

the inner loop asks: is there any start j such that s[j:i] is a word and the part before j is already segmentable?

leetcode
- outer loop starts i = 1, then go into inner loop

j = 0, check dp[0] and s[0:1] - which checks s[0] which has no matching word - we are out of j values in range(i), so increment outer loop to i = 2, then go into inner loop, keep doing this until i = 4

j = 0, check dp[0] and s[0:4] - s[0:4] maps to leet which is in words and dp[0] is True, so we update dp[i] = True then break
-- The reason we break is we only need to find 1 path to match this condition - even if we could combine different substrings to find the same word we are looking for, we only need one viable path 

["ab", "abcd", "cd"]

s = abcd

dp[2] = True, abcd is a direct match for dp[4], but dp[2] and s[2:4] is also a match later in the loop search, however since there already exists one valid match up to dp[i], thats the only path we need to validate it because the whole point of dp is just checking if there is at least 1 way to dp[i], not how we got there
''' 