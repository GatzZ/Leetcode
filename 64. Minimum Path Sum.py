# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in xrange(m)]
        dp[0][0] = grid[0][0]
        for i in xrange(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in xrange(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])

        return dp[m - 1][n - 1]


# Save Space Solution, drop 1 dimension
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [-1] * n
        dp[0] = grid[0][0]
        for j in xrange(1, n):
            dp[j] = dp[j - 1] + grid[0][j]

        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[n - 1]
