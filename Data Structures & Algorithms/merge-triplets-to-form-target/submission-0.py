class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z = target
        a = b = c = 0

        for t0, t1, t2 in triplets:
            if t0 > x or t1 > y or t2 > z:
                continue
            
            a = max(a, t0)
            b = max(b, t1)
            c = max(c, t2)
        
        return [a,b,c] == target