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

'''

                        "" (0,0)
                           |
                      "(" (1,0)
                     /          \
            "((" (2,0)          "()" (1,1)
                |                   |
          "(()" (2,1)          "()(" (2,1)
                |                   |
          "(())" (2,2) ✓       "()()" (2,2) ✓


When curr gets to 2*n that means it has 1 matching open per 1 matching close

There must be an open before a close, so there has to be open > close count, we also must have the open be the first idx we place to satisfy this rule

We dont need explicit pops since strings are immutable, so when we go back up the stack frame, we return back to what curr originally was in this frame because we are restoring its state - the state of curr isnt preserved when jumping back - strings can only be concatenated to, not modified in the idx level

When we pass "", in tree we have 2 options, to include or not include, the left side of the tree is including the decision, however we never accesss the right side of the initial input because the 2nd condition forces us to always have closed < open, because if there were more closed placed than open, then it would be invalid since a closed paren needs an initial open
- ()) or )() - 2 closed + 1 open

Because of this, even when we backtrack completely to the start for the inital input of "", we dont skip the initial open paren since its required for the output to be valid so we only go down the left side of the tree, where we then ensure the condition remains true and perform skips then

Code
Create res arr

Create bt(curr, open, close) 
- Check whether our len(curr) == 2*n, if so each paren has a valid pair

if open < n, then add an open paren, because we can chain as many open paren as we want, and need n-many open paren in order to build the paren we need
- call bt(curr + "(", open+1, close)

if close < open: - this means if we a closing paren, its a valid addition since there is a matching open paren
    call bt(curr + ")", open, close)
- this condition ensures we dont add a closing paren before a matching open paren exists

call bt("", 0, 0)
return res

Go fully down the left side of the tree recursively calling bt(curr + "(", open+1, close) since it remains valid as long as open < n

Once this condition is no longer true, for example n = 2 and we have (( in curr, then we no longer enter open < n, and move down to close < open, which is now true and call bt(curr+")", open, close+1) twice until we end up building (()) - which in our 2nd call meets the condition of len(curr) == 2*n
- we are concatenating during the call and then checking at the top of the call, so at the top of every call its evaluated, and if it it valid that means it would enter neither if statement so we would need to append to res and return it
''' 
