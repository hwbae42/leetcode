class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(i: int, j: int, k: int) -> bool:
            if k == len(word):
                return True
            
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[k]:
                return False
            
            tmp = board[i][j]
            board[i][j] = '#'

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if dfs(ni, nj, k+1):
                    return True

            board[i][j] = tmp    
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
