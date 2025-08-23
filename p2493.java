class Solution {
    public int minimizeXor(int num1, int num2) {
        int count = 0;
        for (int i = 0; i < 32; i++) {
            if ((num2 & (1 << i)) != 0) {
                count++;
            }
        }
        if (count == 0) {
            return num1;
        }
        int result = 0;
        for (int i = 0; i < 32; i++) {
            if ((num1 & (1 << i)) != 0) {
                result |= (1 << i);
                count--;
                if (count == 0) {
                    break;
                }
            }
        }
        if (count > 0) {
            for (int i = 0; i < 32; i++) {
                if ((result & (1 << i)) == 0) {
                    result |= (1 << i);
                    count--;
                    if (count == 0) {
                        break;
                    }
                }
            }
        }
        return result;
    }
}