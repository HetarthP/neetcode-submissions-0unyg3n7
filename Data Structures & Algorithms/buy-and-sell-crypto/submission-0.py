class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left=0
        maxP=0

        for right in range(1,len(prices)):
            if prices[right]>prices[left]:
                profit= prices[right]-prices[left]
                maxP=max(maxP,profit)

            else:
                left=right
        return maxP


        