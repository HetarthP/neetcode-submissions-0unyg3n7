class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        if target not in nums:
            return False
        seen= {} 

        for num in nums: 

            if num in seen: 
                seen[num]+=1 
            else:
                seen[num]=1 

        if seen[target] > (len(nums)//2):
            return True
        return False