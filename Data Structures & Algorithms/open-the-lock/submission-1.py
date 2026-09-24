class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if '0000' in dead:
            return -1
        

        q = deque([('0000', 0)])
        visited = {'0000'}

        while q:
            combo, turns = q.popleft()
            for i in range(4):
                for move in (1, -1):
                    nextDigit = (int(combo[i]) + move) % 10
                    nxt = combo[:i] + str(nextDigit) + combo[i+1:]
                    if nxt not in dead and nxt not in visited:
                        if nxt == target:
                            return turns+1
                        q.append((nxt, turns+1))
                        visited.add(nxt)
                        
        return -1

        '''
        BFS perform a move up and down, as soon as a valid combination is found then return, unlike backtracking where you find all combinations

        Add initial values into queue and set, then enter queue

        pop value out of queue, check whether the popped value is target - this means after we find the value we
        '''
