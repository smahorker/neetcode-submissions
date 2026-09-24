class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if '0000' in dead:
            return -1
        

        q = deque([('0000', 0)])
        visited = {'0000'}

        while q:
            combo, turns = q.popleft()
            if combo == target:
                return turns
            for i in range(4):
                for move in (1, -1):
                    nextDigit = (int(combo[i]) + move) % 10
                    nxt = combo[:i] + str(nextDigit) + combo[i+1:]
                    if nxt not in dead and nxt not in visited:
                        q.append((nxt, turns + 1))
                        visited.add(nxt)
                        
        return -1

        '''
        BFS perform a move up and down, as soon as a valid combination is found then return, unlike backtracking where you find all combinations

        Add initial values into queue and set, then enter queue

        pop value out of queue, check whether combo == target, if so return moves, we do this here to handle edge cases like '0000', right before we add it to the queue it is technically valid, but any combination that makes it into the queue is known to be valid due to our set check and dead check, loop through the 4 idx of popped val - the 2 possible steps are up and down, so for each of these idx need to perform this move of going up and down

        Convert the current idx into an int, add move, then mod by 10 - this handles the positive and negative case - for when we do 0-1 % 10 thats 9, since thats the remainder
        0-3 % 10 would be -7, not applicable to this problem but for reference

        Need to insert this int into proper position in string, use slicing [i:] gets every idx up to i, so it stops right before the idx we were moving, insert str(nextDigit), then
        go from [i+1:] so we move past this digit and fill in the rest

        Now that we have the number with our move accounted for, check whether this number already exists in the set to prevent repeated work and prevents infinite loops
        - 0000 -> 1000 -> 0000 - this would be an infinite loop where the move keeps inversing, also check whether its in deads since those are invalid moves

        Once both checks pass, add the value to the set to mark it as seen, and add it onto the queue to be moved again - incrementing turns to account for the move we just made

        Cant have the check combo check within this if statement since if a case like '0000' was there, we would never enter this code segment and we would never confirm it as   evaluated

        '''
