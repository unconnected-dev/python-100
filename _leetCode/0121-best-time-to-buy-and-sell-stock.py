#Best Time To Buy And Sell Stock
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

casePrices_1 = [7,1,5,3,6,4]
casePrices_2 = [7,6,4,3,1]

if True:
    def bestTimeToBuyAndSellStock(prices):
        
        min_val = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            elif prices[i] - min_val > max_profit:
                max_profit = prices[i] - min_val
        

        print(f"Max profit: {max_profit}")
    
    bestTimeToBuyAndSellStock(casePrices_1)
    bestTimeToBuyAndSellStock(casePrices_2)