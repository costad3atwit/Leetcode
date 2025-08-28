#Problem num.121

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = prices[0]-buy_price
        for price in prices[1:]:
            if price < buy_price:
                buy_price = price
            if price-buy_price > profit:
                profit = price-buy_price        
        return profit
    
