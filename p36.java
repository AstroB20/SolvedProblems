class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[] seen = new boolean[9];
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c != '.') {
                    int index = c - '1';
                    if (seen[index]) return false;
                    seen[index] = true;
                }
            }
            seen = new boolean[9];
        }
        for (int j = 0; j < 9; j++) {
            for (int i = 0; i < 9; i++) {
                char c = board[i][j];
                if (c != '.') {
                    int index = c - '1';
                    if (seen[index]) return false;
                    seen[index] = true;
                }
            }
            seen = new boolean[9];
        }
        for (int boxRow = 0; boxRow < 3; boxRow++) {
            for (int boxCol = 0; boxCol < 3; boxCol++) {
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        char c = board[boxRow * 3 + i][boxCol * 3 + j];
                        if (c != '.') {
                            int index = c - '1';
                            if (seen[index]) return false;
                            seen[index] = true;
                        }
                    }
                }
                seen = new boolean[9];
            }
        }
        return true;   
    }
}