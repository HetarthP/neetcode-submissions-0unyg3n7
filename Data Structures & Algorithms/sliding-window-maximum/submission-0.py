class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        res=[] 

        for i in range(len(nums)-k+1):

            max_num= nums[i]

            for j in range(i,i+k):

                max_num= max(max_num, nums[j])

            res.append(max_num)
        return res


            


        