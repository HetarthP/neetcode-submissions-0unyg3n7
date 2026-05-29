class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        res=[] 

        for i in range(len(nums)):

            res.append(nums[i])

        
        for j in range(len(nums)):

            res.append(nums[j])

        return res
        