class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        #total num of combos that add up to amount 

        #unlimited amount so multiple combos with the same coin 

        dp= [0]*(amount+1)


        dp[0]=1 

        for c in coins:

            for i in range(c,amount+1):

                if i-c>=0:

                    dp[i]+= dp[i-c]
        return dp[amount] if dp[amount]!= float("inf") else 0