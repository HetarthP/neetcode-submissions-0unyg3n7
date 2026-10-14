class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst: bool) -> int:
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                m = l + ((r - l) // 2)
                if nums[m] == target:
                    ans = m
                    if isFirst:
                        r = m - 1
                    else:
                        l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return ans

        return [findBound(True), findBound(False)]