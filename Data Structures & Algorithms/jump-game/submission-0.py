class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) -2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0


'''
The value at goal doesnt matter, as long as we are able to jump to it or past it is all that matters

Loop through the list backwards, try to find if there is a way to the last number or past it by going through the list, start at the 2nd last number because we know regardless the last value will >= goal, since even if its 0, it will be == to goal or non zero will be > goal, so its a useless iteration

- Check the current idxs value is associated with how far you can jump and the idx itself represents how far we have jumped so far

If we have verified that i + nums[i] >= goal, then we have found a valid route to goal, so we can set goal = i, because from i there is a route to goal or past it, we then need to find whether there is a route earlier in the list to this new goal or past it because we choose how far we jump

[1,2,0,1,0]

start at 2nd last nmbr = 1, thats a valid route since i =3, so 3 + 1 = 4, and the goal is 4, so we set goal = 3 - now we want to find a way to reach idx 3

0 fails and we move past it

i = 1 num = 2, 1 + 2 = 3, and goal = 3, so we set goal = 1, because we found a valid route to reach idx 3 by using this current jump

i = 0 num = 1, 1 + 0 = 1, and goal = 1, so we found a valid route to reach idx 1 by using this current jump

Now we have exhausted the list and goal == 0, so we can return

goal == 0 means we can start at the initial index and use a jump of our choosing at each index to reach the end or past it

[2,2,3,1,1]

Even though the 1st idx could reach the 2nd last idx and then jump to the goal, there are multiple routes present, so as long as we can reach
one of the valid routes thats all that matters
- Basically any jump that gets us closer to our goal backwards is a solid path to take because we can use a jump of any length, so it's always worth using that path
'''