class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curr_max = curr_min = ans = nums[0]

        for num in nums[1:]:
            temp= curr_max
            curr_max = max(num, curr_max * num, curr_min * num)
            curr_min = min(num, temp*num, curr_min * num)
            ans = max(ans, curr_max)

        return ans



        

            



            

            


     

            
        