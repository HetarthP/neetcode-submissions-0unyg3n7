class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m: 
            return False

        need = [0]*26
        win  = [0]*26
        a = ord('a')

        for ch in s1:
            need[ord(ch)-a] += 1
        for ch in s2[:n]:
            win[ord(ch)-a] += 1

        if win == need:
            return True

        for r in range(n, m):
            win[ord(s2[r])-a] += 1            # add right
            win[ord(s2[r-n])-a] -= 1          # remove left
            if win == need:
                return True

        return False
