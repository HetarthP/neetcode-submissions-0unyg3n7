class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thisMap= {}

        for i, n in enumerate(nums):
            difference= target -n 
            if difference in thisMap:
                return [thisMap[difference], i]    
            thisMap[n]=i
        return