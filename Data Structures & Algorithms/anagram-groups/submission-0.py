class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_result= defaultdict(list)

        for s in strs:
            count=[0]*26 #this is through the max amt of chars in the alphabet
        
            for c in s: 
                count[ord(c)-ord('a')]+=1
        
            key= tuple(count)

            anagrams_result[key].append(s)
        return anagrams_result.values()
        
        