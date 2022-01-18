class Solution(object):
    #v1
    """def maxProfit(self, prices):
        maxProfit = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                currProfit = prices[j] - prices[i]
                if currProfit > maxProfit:
                    maxProfit = currProfit

        return maxProfit"""

    #v2  # python versoin of https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/1564733/Java-Solution-oror-time%3A-O(N)-oror-space%3A-O(1)
    def maxProfit(self, prices):
        maxProfit = 0
        minPrice = max(prices)

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif (prices[i] - minPrice > maxProfit):
                maxProfit = prices[i] - minPrice

        return maxProfit



if __name__ == '__main__':
    test = Solution()
    prices = [[7,1,5,3,6,4], [7,6,4,3,1], [1,2,3]]

    print(test.maxProfit(prices[2]))
