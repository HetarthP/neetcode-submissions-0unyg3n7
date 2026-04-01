class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        hm=list(set(nums1+nums2))
        hm.sort()

        if len(hm)%2==1:
            mid= len(hm)//2
            median= hm[mid]
        if len(hm)%2==0:
            mid=len(hm)//2
            median = (hm[mid - 1] + hm[mid]) / 2

        return float(median)





        