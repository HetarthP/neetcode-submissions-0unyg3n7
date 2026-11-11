class Solution:
    def findKthLargest(self, nums, k):
        

        res=[] 

        heapq.heapify(res)

        for num in nums: 

            heapq.heappush(res, num)

        
            if len(res)>k:
                heapq.heappop(res)

        return res[0] 