class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l = 0  # Pointer to track the minimum price
        maxProf = 0  # Maximum profit
        for r in range(1, len(prices)):  # Iterate through the prices
            if prices[r] > prices[l]:  # If the current price is greater than the minimum price seen so far
                maxProf = max(maxProf, prices[r] - prices[l])  # Calculate profit and update maxProf
            else:
                l = r  # Update the minimum price to the current price if it's lower
        return maxProf

