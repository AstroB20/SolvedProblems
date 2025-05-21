class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        int carry = 1; 
        for (int i = n - 1; i >= 0; i--) {
            digits[i] += carry; 
            if (digits[i] == 10) { 
                digits[i] = 0;
                carry = 1;
            } else {
                carry = 0; 
                break; 
            }
        }

        if (carry == 1) { 
            int[] newDigits = new int[n + 1];
            newDigits[0] = 1; 
            System.arraycopy(digits, 0, newDigits, 1, n); 
            return newDigits;
        }

        return digits; 
        
    }
}