class Solution:
    def letterCombinations(self, digits: str) -> List[str]:


        res=[] 

        hm = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        if not digits:
            return []

        def backtrack(start, comb):

            if len(comb)== len(digits):
                res.append("".join(comb))
                return 

            letters= hm[digits[start]]

            for letter in letters:

                comb.append(letter)

                backtrack(start+1, comb)
                comb.pop()
        backtrack(0,[])

        return res