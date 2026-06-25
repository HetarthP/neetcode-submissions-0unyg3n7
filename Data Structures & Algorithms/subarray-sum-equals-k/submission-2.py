class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count=0
        sums_map = {0: 1}
        summ = 0

        for i in range(len(nums)):
            summ += nums[i]
            if (summ - k) in sums_map:
                count += sums_map[summ - k]
            sums_map[summ] = sums_map.get(summ, 0) + 1
        return count