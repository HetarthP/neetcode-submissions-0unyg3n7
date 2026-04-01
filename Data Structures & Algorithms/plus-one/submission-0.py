class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: 
        
        new_num=0
        
        new_s= ''.join(str(d) for d in digits)
        new_num= int(new_s)+1

        res= [int(char) for char in str(new_num)]

        return res
        
        

            


        