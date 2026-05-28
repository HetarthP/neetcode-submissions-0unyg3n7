class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

        res=[0]*len(arr)

        right= -1

        for i in range(len(arr)-1,-1,-1):

            res[i]= right
            right= max(right, arr[i]) 
        return res 

        