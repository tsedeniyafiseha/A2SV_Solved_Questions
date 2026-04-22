class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited=set()
        rows,cols= len(grid),len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(r, c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return 1
      
            if grid[r][c]!=1:
                return 1
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            perimeter = 0
            for dr, dc in directions:
                perimeter += dfs(r + dr, c + dc)

            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                   return dfs(r,c)
        return 0