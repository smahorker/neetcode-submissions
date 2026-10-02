class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r == row or c < 0 or c == col or word[i] != board[r][c] or (r, c) in path:
                return False
            
            path.add((r, c))
            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))

            path.remove((r,c))
            return res
        
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False


'''
Checking a word starting from idx 0, then going down all possible adjacent nodes to see if its a valid path

Using a visit set to mark what has been added to the path

Create dfs function to traverse neighboring nodes, pass in row idx, col idx, and searched for letter, this tell us where we are across dfs nested dfs calls and what our target letter is

Exit when the letter idx matches length of the word

Check whether the adjacent node is valid to traverse - within bounds, the character we are looking for, and the traversed idx doesnt exist in path
- we need to check whether the traversed doesnt idx in path for infinite loops and say we were looking for "baa", and we were on the 2nd a, we might jump back to the first a if we didnt validate it was a unique index - since it was the character we were looking for but it was a duplicate

'''