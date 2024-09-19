class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        high = 0
        
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            if prices[i] - low > high:
                high = prices[i] - low
        
        return high
                