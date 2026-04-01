class Solution:
    def longestPalindrome(self, s: str) -> str:

        res= ""
        resLength=0 


        for i in range(len(s)):

            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                window= r-l+1
                if window>resLength:

                    res=s[l:r+1]
                    resLength=window
                l-=1
                r+=1
            
            l,r=i,i+1

            while l>=0 and r<len(s) and s[l]==s[r]:
                window=r-l+1
                if window>resLength:

                    res=s[l:r+1]
                    resLength= window
                l-=1
                r+=1
        return res 

        