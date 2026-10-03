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
When i == len(matchsticks) it means we've found a route to exhaust all matchsticks
- we still go through the list in order, however when we pass the last element, that means we found a valid route - otherwise we wouldnt have called bt(i+1) on it

'''