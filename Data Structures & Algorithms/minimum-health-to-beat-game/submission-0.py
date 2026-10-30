class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        total= sum(damage) 

        blocked= min(max(damage), armor)

        return total- blocked+1