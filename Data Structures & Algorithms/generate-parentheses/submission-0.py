class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def bt(curr, open, close):
            if len(curr) == 2*n:
                res.append(curr)
                return

            if open < n:
                bt(curr + "(", open+1, close)
            
            if close < open:
                bt(curr+")", open, close+1)
        
        bt("", 0, 0)
        return res