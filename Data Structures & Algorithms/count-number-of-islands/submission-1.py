class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows:int = len(grid)
        columns:int = len(grid[0])

        def dfs(row, column) -> None:

            if row < 0 or row >= rows or column < 0 or column >= columns or grid[row][column] == "0":
                return
            else:
                grid[row][column] = "0"
                dfs(row, column+1)
                dfs(row+1, column)
                dfs(row, column-1)
                dfs(row-1, column)

        num_islands:int = 0

        for row in range(0, rows):
            for col in range(0, columns):
                cell_value = grid[row][col]
                if cell_value == "1":
                    num_islands += 1
                    dfs(row, col)


        return num_islands
        