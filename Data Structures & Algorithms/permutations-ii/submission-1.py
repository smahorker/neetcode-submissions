class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                path.append(nums[i])

                backtrack()

                path.pop()
                used[i] = False
        
        backtrack()
        return res



'''
Use a bool array to track whether something has been used
- if a number is a duplicate and the previous one has been marked, then its fine to reuse since the duplicates are in use for this singular path, however if it is a duplicate and the previous idx has not been marked as used in current path, then that path has already been explored and we are moving past it

Only when we first encounter the value that has future duplicates do we create the permutation, then from that point onward we move past that number, because it will just go down duplicate paths that we already visited and clog res

In permutations, each backtrack() call loops through the entire list starting from index 0, rather than from a start pointer. This means that even if the first number chosen sits in the middle of the list, later slots can still pick numbers from earlier in the list. The used[i] array keeps us from picking the same element twice. So say we have [1,2,3] - we eventually want the perm [2,1,3] and the initial value would be 2, so we would need to go to the start of the list to add the 1
- We dont pass a start variable here because we loop back to the start of the list in every callback to see if there are any unused indicies we want to use

We find [1a,1b,2] then we pop 2, set it to False, there is nowhere else in the for loop to go so we return, then we pop 1b, set it to False, and now i = 2 and the path is [1a] and since used[2] is now False, we append - [1a, 2] then call backtrack and since used[0] is T, we append - [1a, 2, 1b], record because of base case and return, pop 1b - set to false - loop moves fwd 1 iteration i =2 but i=2 in use so continue which returns, unchoose 2 and set false, unchoose 1 and set false
- Original loop now moves fwd 1 iteration, [F,F,F] but on idx 1 which is 1b, its not used, but fails the duplication check, so we move the original loop to start off with 2, making used as [F,F, T]
'''