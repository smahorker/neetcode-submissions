class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def btr(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for i in range(start, n + 1):
                comb.append(i)
                btr(i+1, comb)
                comb.pop()
        btr(1, [])
        return res

'''
Go through value by value building a combination list at each iteration, once a combination hit reaches a size of k
then we can remove it from the list and remove the most recent added value, the reason we remove the most recently added
value is because thats the limiting value in creating the next unique combination - we delete any deeper because
then we would potentially create duplicates - 2 3 7 but if we deleted 2 deep then we could get 2 7 3 in a future iteration when going through

Once youve constructed the first valid combination, append the value to the result list since its valid and wont change,
since the value has been added we can then pop, and move onto the next value - btr(i+1, comb) handles updating the
value of start so that our range function doesn't reset every time we go a level deeper in the call stack
- This loop ensures that we are only going in increasing order for the next value we explore, each time we add a value
to comb, we check whether len(comb) > k, if so we found a valid combination and we also pop the last idx inside of comb
to find more combinations

-- We do this until we've exhausted all the valid combinations of having our current 0th idx, once we move past this 0th
idx, we will never see it again, since the list only goes in increasing order

When we call btr(1, []) we then check all combinations having [1] as thats the first value we append on, then the next
line after that is a recursive call to check all combinations that have [1] as idx 0 so it calls (2, [1]) then (3, [1])..., once thats finished we then pop [1] since we've returned from the final part of that call stack, so since 
we're in a for loop it moves onto start = 2, so then we get comb = [2] and we call btr(2+1, [2]) and continue until
this for loop is complete and we finally return res
'''