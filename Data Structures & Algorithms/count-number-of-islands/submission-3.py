class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        
        rows:int = len(grid)
        columns:int = len(grid[0])


        def dfs(row, col) -> None:
            
            if row < 0 or row >= rows or col < 0 or col >= columns or grid[row][col] == "0":
                return

            else:
                grid[row][col] = "0"
                dfs(row, col + 1)
                dfs(row + 1, col)
                dfs(row, col - 1)
                dfs(row - 1, col)
        
        num_islands:int = 0

        for row in range(0, rows):
            for col in range(0, columns):
                cell_value:int = grid[row][col]
                if cell_value == "1":
                    num_islands += 1
                    dfs(row, col)

        return num_islands
        