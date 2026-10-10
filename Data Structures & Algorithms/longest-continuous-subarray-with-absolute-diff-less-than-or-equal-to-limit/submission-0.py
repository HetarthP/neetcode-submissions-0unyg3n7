class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        longest=0 

        l=0 

        maxDeque = deque()
        minDeque = deque()

        for r in range(len(nums)):

            while maxDeque and nums[r] > maxDeque[-1]:
                maxDeque.pop()

            maxDeque.append(nums[r])

            while minDeque and nums[r] < minDeque[-1]:
                minDeque.pop()

            minDeque.append(nums[r])

            while maxDeque[0] - minDeque[0] > limit:
                if maxDeque[0] == nums[l]:
                    maxDeque.popleft()
                if minDeque[0] == nums[l]:
                    minDeque.popleft()
                l += 1
                    
            longest = max(longest, r-l+1)
        return longest