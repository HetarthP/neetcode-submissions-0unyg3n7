class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)>1: return [0]* len(nums) #checks that if theres more than 1 0, return all the 0's in the list

        product= math.prod(nums) # create product of the whole list
        prod_without_0= 1 #create standard variable to set to 1 if there's no 0 in the list since it'll multiply by 1 which is just itself

        for n in nums: 
            if n==0: continue 
            prod_without_0 *=n #loop through and if the index is 0, continue through otherwise ultiply all the non-zero products 

        res=[]

        for n in nums:

            if n==0:
                res.append(prod_without_0)#append non-zero product if there is an index which is - in the list
            else:
                res.append(int(product/n)) #append the actual product which is the total product divided by the index number as an integer and not float 

        return res