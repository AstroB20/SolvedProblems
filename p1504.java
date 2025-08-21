class Solution {
    public int numSubmat(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int[][] dp = new int[m][n];
        int count = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) {
                    dp[i][j] = (i == 0 ? 0 : dp[i - 1][j]) + 1;
                }
                int minHeight = dp[i][j];
                for (int k = j; k >= 0; k--) {
                    minHeight = Math.min(minHeight, dp[i][k]);
                    count += minHeight;
                }
            }
        }
        return count;
    }
}