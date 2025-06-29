class Solution {
    public int numSubseq(int[] nums, int target) {
        Arrays.sort(nums);
        int mod = 1000000007;
        int n = nums.length;
        int left = 0, right = n - 1;
        long res = 0;
        long[] pow = new long[n];
        pow[0] = 1;
        for (int i = 1; i < n; i++) {
            pow[i] = (pow[i - 1] * 2) % mod;
        }
        while (left <= right) {
            if (nums[left] + nums[right] <= target) {
                res = (res + pow[right - left]) % mod;
                left++;
            } else {
                right--;
            }
        }
        return (int) res;
    }
}