class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        #days of year = days 

        #always 3 costs - 1 day= first, 7 day = 2nd, 30 day= 3rd 

        #basically min cost to travel all the days 

        dp= [0]*((len(days))+1)

        for i in range(len(days)-1,-1,-1):
            dp[i]= float("inf")
            j=i 

            for d,c in zip([1,7,30],costs):
                while j<len(days) and days[j]<days[i]+d:
                    j+=1
                dp[i]= min(dp[i], c+dp[j])
        return dp[0] 


        