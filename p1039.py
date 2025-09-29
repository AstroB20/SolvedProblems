class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for length in range(2,n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i+1,j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[j] * values[k]
                    dp[i][j] = min(dp[i][j],cost)
        return dp[0][n - 1]