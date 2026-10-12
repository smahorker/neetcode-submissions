class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0

        return start


'''
Any route that is less cost and more gas gain is a viable starting point

If the sum of costs > sum of gas, that means there is no way to incur all the costs at each station to make a round trip

Set start to 0 and tank to 0

Start from idx 0 and loop through all the values

Calculate the net cost of visiting this station - getting the gas and leaving
- If our tank < 0 after this visit, that means the current station and every station before it is a non viable route

-- For us to even consider starting at a station, it must have been a positive station, any station thats a positive will only help us in our round trip, so we want to keep them - only future stations we visit after the initial may incur more costs than fuel gain

Say we started at station a and got to d, station a would have to be a positive gain and by d we were at a negative tank, even if we start at i + 1, so station b, this would lead to only a further negative tank, as our initial value was positive - so we can remove this entire route and move to i + 1, which would check station e

Since sum(gas) > sum(costs), there has to be some viable route, we would have gas left over after incurring the cost of every station

Setting start = i + 1 before we even enter the next iteration is fine if our tank is empty because we know thats when we are always going to reset our tank, so we do it here before we calculate our new tank value because doing at the very start of the loop would make no sense - for the 0th iteration it would always enter so its just an extra condition and we would move tank calculation under
'''