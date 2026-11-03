class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable_set, prev_height):
            # Check boundaries, if already visited, or if it's downhill (invalid reverse path)
            if (r < 0 or r >= m or c < 0 or c >= n or
                    (r, c) in reachable_set or heights[r][c] < prev_height):
                return

            # Mark current cell as reachable from this ocean
            reachable_set.add((r, c))

            # Traverse all 4 cardinal directions (North, South, East, West)
            dfs(r + 1, c, reachable_set, heights[r][c])
            dfs(r - 1, c, reachable_set, heights[r][c])
            dfs(r, c + 1, reachable_set, heights[r][c])
            dfs(r, c - 1, reachable_set, heights[r][c])

        # 1. Trigger DFS from the Top and Bottom borders
        for c in range(n):
            dfs(0, c, pacific_reachable, heights[0][c])  # Top Row (Pacific)
            dfs(m - 1, c, atlantic_reachable, heights[m - 1][c])  # Bottom Row (Atlantic)

        # 2. Trigger DFS from the Left and Right borders
        for r in range(m):
            dfs(r, 0, pacific_reachable, heights[r][0])  # Left Column (Pacific)
            dfs(r, n - 1, atlantic_reachable, heights[r][n - 1])  # Right Column (Atlantic)

        # 3. Collect coordinates that are present in both sets
        result = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])

        return result


# ==========================================
# RUNNING TEST CASES
# ==========================================
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Standard Example Grid
    # Pacific is Top & Left. Atlantic is Bottom & Right.
    grid1 = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]

    expected_output1 = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    result1 = sol.pacificAtlantic(grid1)

    print("Test Case 1:")
    print("Calculated Coordinates:", sorted(result1))
    print("Expected Coordinates:  ", sorted(expected_output1))
    print("Match Status:          ", sorted(result1) == sorted(expected_output1))

    print("\n" + "-" * 40 + "\n")

    # Test Case 2: Monolithic Single Cell Grid
    grid2 = [[1]]
    expected_output2 = [[0, 0]]
    result2 = sol.pacificAtlantic(grid2)

    print("Test Case 2 (Single Element):")
    print("Calculated Coordinates:", result2)
    print("Match Status:          ", result2 == expected_output2)