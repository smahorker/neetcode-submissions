class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side = total // 4
        if max(matchsticks) > side:
            return False
        
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def bt(i):
            if i == len(matchsticks):
                return True
            seen = set()
            for j in range(4):
                if sides[j] in seen:
                    continue
                if sides[j] + matchsticks[i] > side:
                    continue
                seen.add(sides[j])

                sides[j] += matchsticks[i]
                if bt(i+1):
                    return True
                sides[j] -= matchsticks[i]
            return False
    
        return bt(0)


'''
Calculate total and see if we can create 4 equal sides and ensure that the largest number in the list is not bigger than any of the sides

Sort it in reverse order because the larger elements are more likely to end their branches earlier - 7+2 vs 1+2+5 - both reach 9  but the route that needs only 2 numbers reaches it faster

When i == len(matchsticks) it means we've found a route to exhaust all matchsticks
- we go through the list in order, however when we pass the last element, that means we found a valid route - otherwise we wouldnt have called bt(i+1) on all the previous iterations as they would have failed the sides[j] checks

Create a new set for each recursive call, we dont need to try putting a stick on a size length we have already seen before, because the path it will produce from this idx will always be the same - sides = [2,2,1,0] - trying to add 1 - we try 2+1 path, we dont need to try sides[1] because we tried the same path in sides[0], so its just repeated work so use the set to indicate we've already went down that path, but we still need to try 1 and 0 since theyre unique
-- When we do add the stick - we are choosing to only add the stick to that in this bt path, so we try [3,2,1,0] or [2,2,2,0] or [2,2,1,1] and see if any of those lead to a valid path - we skip [2,3,1,0] because it would produce the same result as [3,2,1,0]

Check whether adding the stick passes the side value, if it does then adding this stick to this side - lets say L - sides[0] would cause the side to be too large, so we would need to try it on another side and see if it fits, we would try it on R - sides[1] next for example because we used continue which moves to the next loop iteration so j increments by 1 and doesnt execute the rest of the code

Once this check passes, that means we found a valid place to put our stick, so we add the stick to the current side and and call bt(i+1) from bt(3) lets say to move to the next stick in our list, we go down this path until we determine if it is valid, if it is then we short circuit return True and exit but if its False then we subtract up the call stack unchoosing all the decisions we made on that path and return to bt(3) restoring our path, we also need to subtract the decision we made that led us to bt(i+1) because we decided to unpick it and increment j since the path was invalid - so we want to move past this decision and try to see if the stick is valid on a different side which produces a new path

If we traverse down all paths and they are invalid then we return False - keep in mind when we unwind once lets say from bt(5) up to bt(4) for a list of size 8, there are still multiple indicies for bt(4) to traverse, so it runs its own recursive calls and increments j down that path to see if this subpath is valid

Call bt(0) since thats the initial index

'''