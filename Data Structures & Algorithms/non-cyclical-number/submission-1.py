class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # to detect loops

        while n != 1:
            if n in seen:
                return False  # we've looped → not happy
            seen.add(n)

            # replace n by the sum of the squares of its digits
            n = sum(int(digit)**2 for digit in str(n))
        
        return True
