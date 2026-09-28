class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = (r-l) + 1
                l -= 1
                r += 1
        return res
    

'''
Treat a character as the middle and compare whats to the left and right of it and expand outwards, since a character by itself is a palindrome, then it's a valid starting point, however a position only has 2 adjacent characters when its odd, for example idx 1 has 2 adjacent of 0 and 2, we also need to deal with the case of treating the substring as a mirror of itself - since thats how even length palindromes work

- As we add the adjacent position for odd positions, we go from size 1, to size 3, to size 5 - which skips over the palindrome case of being mirrored over each other - 'aa', so get i and i +1 - i + 1 holds starting from idx 0 over i-1 which would go out of bounds, which handles the cases of size 2, size 4, ... from our starting idx

xxaaxx

0 - odd - x | e - xx
1 - o - x | e - f
2 - o - a | e - start aa, then xaax, then xxaaxx

Need to account for the substring expanding in all sizes, not just 1,3,5..., we deal with 2,4,... by including the next idx in our substring, and over extension in last idx is accounted for in the if statement
'''