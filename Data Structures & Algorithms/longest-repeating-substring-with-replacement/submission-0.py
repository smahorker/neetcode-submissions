class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                
                while (r-l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                res = max(res, r - l + 1)
        return res
'''
Create a set of the unique characters present, there can be only 26 total different
english characters so its O(26N traversal) - we are going to test each character
one by one

Look through, we are looking for duplicates ideally and only exiting out after k amount
of non duplicates have been found

So we loop through the input string, check whether the right ptr is actually on
the character we are currently inspecting
- if it is, then we iterate the count by one - this count is our reference point
for how many of the same character we've seen

- if its not and we havent exceeded past k, then move one more iteration in the loop

- if its not a duplicate and we have exceeded past k, which we measure through (r-l + 1)
in order to get the window size (+1 because its 0 based indexing so 2-0 is actually
3 values)
-- so if the window - count is larger than k, we've encountered more non duplicates
than allowed, so we need to loop through and go until we've gotten rid of enough 
non duplciate values

--- Even if this means we are going to get rid of duplicate values, we have to because
the window string is in an invalid state xxxssx k = 1, we would need to start
removing once we hit the 2nd s, but we've already tracked the max in our state variable
res, so we return to a valid state to check whether a better solution exists

return res which is the max we've found across all characters since its outside
window loop scope
'''