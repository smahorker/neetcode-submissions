class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                pcopy = p.copy()
                pcopy.insert(i, nums[0])
                res.append(pcopy)
        return res

'''
Go from full list and narrow element by element into base case

Insert the first element of each iteration into each position of the existing lists, this is because
a new permutation can be made with each of these positions

The number previous to it will propogate into having lists in it because when we are inserting the values, we are
creating a copy, so the previous iterations values get copied over

Starting from full list, narrowing down value by value til we hit base case, then going up the call stack starting with
the last idx, inserting based on loop condition, moving up to the next value, then inserting it based on loop condition
etc until list is complete

Res is different on each call stack, so appending to res doesnt matter until we finally return

The length of our list parameter determines how many insertions we do, so we may only need to insert once if
the len is 0, or if the len is 2 we would need to insert at the back, middle, and end bc len(p) + 1

The outer for loop handles multiple permutation lists, so if we have [2,3] and [3,2] thats handled so we first go
through 2,3 and insert 1 in there first, then move onto inserting 1 for 3,2 - our funciton returns res so permute([1,2,3]) would return [[2,3] , [3,2]] and only after 1 is inserted we are done with our call stack and return
all permutations
'''