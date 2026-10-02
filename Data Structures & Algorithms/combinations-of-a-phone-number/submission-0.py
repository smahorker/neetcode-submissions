class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }

        res = []
        path = []

        def bt(i):
            if i == len(digits):
                res.append("".join(path))
                return
            
            for letter in phone[digits[i]]: # loop over all the letters in the associated digit - 2 : abc - loop through a,b,c
                path.append(letter)
                bt(i+1)
                path.pop()
            
        bt(0)
        return res
            

'''
23

The initial state of the path = [], which is the same as starting off at "" in the decision tree, when we decide to call bt(0) passing in idx 0, then we have the options of a b c

start at idx 0, so 2 and backtrack from there, set the base case of when i == len(digits), then we add it to the res, because for it to be a valid addition there has to be 2 digits

We use path to build up to the expected amount of digits, then backtrack to deselect

              ""
         /    |    \
        a     b     c         <- choices for digit '2'
      / | \ / | \ / | \
     d  e f d e f d e f       <- choices for digit '3'

'''
