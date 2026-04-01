class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm= collections.defaultdict(list)

        for s in strs:
            hash= str(sorted(list(s))) #sorting the chars in the string

            hm[hash].append(s) #adding original string to its sorted one

        return list(hm.values())# returning it as a list of values



