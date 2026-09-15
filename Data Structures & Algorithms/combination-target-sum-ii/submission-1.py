class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res

        
        
        '''
        Sort the list of numbers so we can easily move past duplicates

        We have 2 options, move to the next number, or choose to not use that number and skip it

        Our stopping conditions are we meet our target and append a copy to our res, our total surpasses the target or
        we have reached the end of the list of numbers

        1. Add the initial value, which starts at 0 in the dfs call
        2. Recursively call our helper function on this, going forward 1 idx at a time, passing in the cur combination, and
        updating the total value
        3. The left branch goes down summing up each value sequentially until the stopping condition is met, once it is then
        we return, after this return we then pop latest value
        3.5. After we found a valid combination, any other numbers we test against it with the prefix of numbers with the value
        now missing will always be invalid [1,2,3] -> [1,2] -> [1,2,7] for target 6, only the original combination works
        4. The while loop causes this to be technically excess work, but its important for the duplicate case, because 
        when we decide not to use candidate[i], we want to skip over all occurances of it
        4.5. if we do decide to use candidate[i] it only matters from the point at which we want to keep using it, 
        like choosing a 3rd duplicate serves the same purpose as the first appearance since theyre the same value

         the pop sets us up, its essentially undoing the move and bringing us back up to the parent, then the while loop moves 
         us past duplicates and then the dfs call brings us into that branch

         candidates[i] == candidates[i+1] - this stops at the last duplicate, so we need to move past it with i + 1 in the dfs call
        '''
