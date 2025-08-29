class Solution {
    public long flowerGame(int n, int m) {
        long[][] dp = new long[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                dp[i][j] = Math.max(dp[i - 1][j] + i, dp[i][j - 1] + j);
            }
        }
        return dp[n][m];
    }
}