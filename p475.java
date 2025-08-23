class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        Arrays.sort(houses);
        Arrays.sort(heaters);
        int radius = 0;
        int j = 0;
        for (int i = 0; i < houses.length; i++) {
            while (j < heaters.length - 1 && Math.abs(houses[i] - heaters[j]) >= Math.abs(houses[i] - heaters[j + 1])) {
                j++;
            }
            radius = Math.max(radius, Math.abs(houses[i] - heaters[j]));
        }
        return radius;
    }
}