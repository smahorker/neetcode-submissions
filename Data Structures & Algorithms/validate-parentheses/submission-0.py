'''
Use a stack to track open parentheses, add to stack as open keeps on adding,
once you encounter a close paren, compare with top of stack to see if that matches
in the dictionary, if it does then pop otherwise return false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CloseOpen = { "]":"[", "}":"{", ")":"(" }

        for c in s:
            if c in CloseOpen:
                if stack and stack[-1] == CloseOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
