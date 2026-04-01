class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        target = sorted(s1)

        k = len(s1)

        for r in range(len(s2) - k + 1):

            res = sorted(s2[r:r+k])

            if target == res:
                return True

        return False