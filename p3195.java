class Solution {
    public int minimumArea(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int minArea = Integer.MAX_VALUE;

        for (int left = 0; left < n; left++) {
            for (int right = left; right < n; right++) {
                int top = -1;
                int bottom = -1;
                for (int row = 0; row < m; row++) {
                    boolean hasOne = false;
                    for (int col = left; col <= right; col++) {
                        if (grid[row][col] == 1) {
                            hasOne = true;
                            break;
                        }
                    }
                    if (hasOne) {
                        if (top == -1) {
                            top = row;
                        }
                        bottom = row;
                    }
                }
                if (top != -1) {
                    int area = (right - left + 1) * (bottom - top + 1);
                    minArea = Math.min(minArea, area);
                }
            }
        }

        return minArea == Integer.MAX_VALUE ? 0 : minArea;

    }
}