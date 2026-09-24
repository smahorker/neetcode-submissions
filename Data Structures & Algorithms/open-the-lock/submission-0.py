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
                        q.append((nxt, turns+1))
                        visited.add(nxt)
        return -1

