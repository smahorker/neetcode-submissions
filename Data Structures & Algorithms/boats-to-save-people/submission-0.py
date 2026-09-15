class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0

        while l <= r:
            total = people[l] + people[r]
            if total > limit:
                r -= 1
                res += 1
            else:
                res += 1
                l += 1
                r -= 1
        return res
