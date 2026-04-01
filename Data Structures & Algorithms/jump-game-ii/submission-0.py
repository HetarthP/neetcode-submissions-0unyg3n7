class Solution:
    def jump(self, nums: List[int]) -> int:
        

        n= len(nums)

        target= n-1 

        count= 0 

        while target>0:

            for i in range(0, target):

                max_jump= nums[i]

                if i + max_jump >= target:
                    count+=1
                    target = i
                    break

        return count
