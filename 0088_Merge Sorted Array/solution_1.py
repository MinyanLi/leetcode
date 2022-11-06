# Runtime 78 ms Beats 32.52%
# Memory 14 MB Beats 5.93%

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            nums1[~i] = nums2[i]

        nums1.sort()
