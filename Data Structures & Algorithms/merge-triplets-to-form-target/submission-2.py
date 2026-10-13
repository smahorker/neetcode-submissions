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


'''
We can only performa a max check and we perform a max check on each of the elements between a paired triplet and we need to perform the check on every element
- If any element in the triplet is > target, that means it needs to be pruned since if we perform a max check on another triplet, this higher than target value is going to be sustained

merging triplets e,f,g outputs triplet d - this triplet d is going to be now stored in variables a,b,c and we compare a,b,c against every value in any future triplet we see, and since we prune out any triplet with a value > target for its associated idx, then we know the value present in the new triplet can only be between 0 to target idx value

Onced we've gone through every element in the list, we have a list of numbers that are either == target or have triplet indicies that are less than the target - this is guaranteed because we removed any value > target index value in our loop from being processed
- If the list matches up, then we return target
'''