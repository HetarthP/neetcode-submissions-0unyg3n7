class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=[]

        def backtrack(start, comb):

            if sum(comb) == target:
                res.append(comb.copy())
                return 
            
            if sum(comb) > target:
                return
            
            for i in range(start, len(nums)):

                comb.append(nums[i])

                backtrack(i, comb)

                comb.pop()
        backtrack(0,[])

        return res