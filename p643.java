class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int n = nums.length;
        double maxAverage = -1000000; 
        double currentSum = 0;
        for (int i = 0; i < k; i++) {
            currentSum += nums[i];
        }
        maxAverage = Math.max(maxAverage, currentSum / k);
        for (int i = k; i < n; i++) {
            currentSum += nums[i] - nums[i - k];
            maxAverage = Math.max(maxAverage, currentSum / k);
        }

        return maxAverage;        
    }
}