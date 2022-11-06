# Runtime 83 ms Beats 99.57%
# Memory 14.2 MB Beats 67.80%

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 != 0:
            return float(nums[len(nums)//2])
        if len(nums) % 2 == 0:
            n = int(len(nums)/2)
            return float("{:.5f}".format((nums[n - 1] + nums[n]) / 2))
