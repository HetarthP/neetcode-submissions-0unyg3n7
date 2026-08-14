class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        #return a subset of the strings that add up the chars to m,n


        count=0 

        dp= {(0, 0): 0}  # (zeros, ones) : max_subset_size


        for i in range(len(strs)):

            first= strs[i].count("0")
            second= strs[i].count("1")

            next_dp= dp.copy()

            for (cur_z, cur_o), size in dp.items():

                new_z= cur_z+first
                new_o= cur_o +second

                if new_z<=m and new_o<= n:
                    next_dp[(new_z, new_o)] = max(next_dp.get((new_z,   new_o), 0), size + 1)
            dp = next_dp
        
        return max(dp.values())