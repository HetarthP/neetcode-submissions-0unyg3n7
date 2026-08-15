class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        

        #any two stones
        #return smallest, so optimize basically

        summ= sum(stones)

        total= summ//2

        dp= [0]*(total+1)

        for stone in stones:

            for i in range(total, stone-1, -1):
                dp[i]= max(dp[i], dp[i-stone]+stone)
        return summ-2*dp[total] 