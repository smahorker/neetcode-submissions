class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        ''' its 1 and not min(piles) because we dont need to finish a pile within
        1 hour, we can take multiple hours to finish 1 pile as long as its within
        the total hour limit'''
        while l <= r:
            mid = (l+r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / mid)
            
            if time <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

         