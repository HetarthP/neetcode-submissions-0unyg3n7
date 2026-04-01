from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        count = Counter(hand)
        hand.sort()

        for card in hand:
            if count[card] == 0:
                continue

            # build one group starting at the smallest available card
            for x in range(card, card + groupSize):
                if count.get(x, 0) == 0:
                    return False
                count[x] -= 1

        return True
