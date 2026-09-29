class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def dp(i: int) -> int:
            if i == n:
                return 1
            if i in memo:
                return memo[i]
            if s[i] == '0':
                memo[i] = 0
                return 0

            ways = dp(i + 1)
            if i + 1 < n and int(s[i:i+2]) <= 26:
                ways += dp(i + 2)

            memo[i] = ways
            return ways

        return dp(0)

'''
dp(i) stores the number of valid ways to decode the suffix s[i:], from index i to the end. At dp(1), choosing "12" consumes indices 1 and 2, so the remaining problem starts at index 3. dp(3) already holds the number of ways to decode what's left after "12", so dp(1) adds that value to its total.

The memo is a record of work we've already done, so it's the past of the computation, but each entry describes the part of the string after its index.

We call ways = dp(i+1) until we reach the end of our arr + 1, 1123 would be dp(4) - 0-3 idx, which hits our base case of i == n, where we return 1, this return goes up 1 level in the call stack as we unwind

Now at dp(3), since we returned 1 from dp(4) on ways, we then check the if statement to see if we can take a 2 digit value, which we cant since there is only 1 digit, which is 3 in 1123, so we assign memo[3] = 1, so we know from the idx 3, there is exactly 1 way - now we move up the call stack

dp(2), none of the base cases hit, call ways = dp(2+1) = dp(3), which is a hit on memo, so set ways = 1, now move back into dp(2) since that sub call was complete, then check the condition, which is valid on "23", we call dp(2+2) = dp(4) which hits a base case and returns 1, which means we accumulate another 1 on ways, so 1+1 = 2, which we store in memo for memo[2] = 2

dp(1), none of  the base cases hit, call ways dp(1+1) = dp(2) = 2, then on "12" call dp(1+2) = dp(3) = 1 and accumulate again, so 2+1 = 3

dp(0), dp(1) = 3, dp(2) = 2 - 3+2 = 5


                                  dp(0) "1123"
                          /                            \
                 dp(1) "123"                        dp(2) "23"
                /           \                      /          \
        dp(2) "23"       dp(3) "3"          dp(3) "3"        dp(4) ""
         /       \            |                  |
 dp(3) "3"    dp(4) ""    dp(4) ""           dp(4) ""
     |
 dp(4) ""


If it was just a 4 digit number, there would be only 1 way to decode it since the 2 digits have no new mapping
- Since it includes 2 digit numbers, we have to look at the current number and the next as we work backwards
-- look at dp(0) - if we were just to use the case of single digit numbers, just adding 1 to 123 would be the same number of ways to decode as 123 would be - this relationship holds true because the number of ways to build 123 relied on 23, then 3, then ""
--- However since we have 2 digit numbers, the ways to decode 123 isnt just a static 1, building 123 relied on the 1 digit and 2 digit decoding, so now that we are looking at 1123, we are essentially adding 11 to 23, how many ways are there to decode 23 since we are adding 11 which has a direct mapping
- each index needs to look at itself as a 1 digit and a 2 digi number because thats the way it can be decoded, thats what adds the variance in total ways of decoding


dp stores the number of ways to decode each suffix. If every digit could only be its own letter, prepending a digit wouldn't change the count. But a valid two-digit chunk gives a second way to start. For "1123", taking 1 (A) leaves "123" with 3 decodings, and taking 11 (K) leaves "23" with 2 decodings (BC or W). Both starts are valid and produce different decodings, so we add them: 3 + 2 = 5.
'''