class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0
        for i in range(1, len(prices)):
            trans = prices[i] - prices[buy]
            if trans > profit:
                profit = trans
            elif prices[buy] > prices[i]:
                buy = i
        return profit