class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return

        rows:int = len(grid)
        columns:int = len(grid[0])

        def dfs(row, col) -> int:

            if row < 0 or row >= rows or col < 0 or col >= columns or grid[row][col] == 0:
                return 0
            else:
                grid[row][col] = 0
                area:int = 1
                area += dfs(row, col+1)
                area += dfs(row+1, col)
                area += dfs(row, col-1)
                area += dfs(row-1, col)
                return area


        max_area:int = 0

        for row in range(0, rows):
            for col in range(0, columns):
                cell_value:int = grid[row][col]
                if cell_value == 1:
                    current_area:int = dfs(row, col)
                    max_area = max(max_area, current_area)

        return max_area
        