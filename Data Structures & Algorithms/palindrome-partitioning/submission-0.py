class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPali(sub):
            return sub == sub[::-1]
        
        def bt(start):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start + 1, len(s) +1):
                piece = s[start:end]
                if isPali(piece):
                    path.append(piece)
                    bt(end)
                    path.pop()
        
        bt(0)
        return res

'''
Create res to store all palindromes

Path to track where we in our list thus far

Helper func to backtrack

When start == len(s) then we append, we do this because that means we've traversed all the possible routes in our path

"aab"
- 3 routes, choose a, aa, or aab

Going down a1, you then loop through and its a valid palindrome, so then it triggers for a2 valid, then b valid, we call bt one more time and the start ==len(s) conditions triggers and we save then we return to bt(2), pop b, so path == ['a', 'a'] and go back to bt(1) where we pop once again and path = ['a'] - we pop here again because we've explored down this path in its entirety the next iteration would be its own path even if it has the same start - the path we went down had 'a' and 'b' and the next path would be a2b which would never be possible down the first path we went, we then increment end and check a2b - start does not move, which is invalid pali, then we exceed the loop limit because of range(2,4) - did (3,4) to reach b, then next iter is (4,4) - we dont auto return bt from a2 to a1 there is still a unique path of a2b which a1 can never reach on its own, also for example aaba, if we went to a1 then a2ba would have never been reached

- We are back to a1, 
'''