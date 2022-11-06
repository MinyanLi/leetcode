# Runtime 121 ms Beats 10.96%
# Memory 14.6 MB Beats 98.85%

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a = - 1
        for i in nums:
            if i < target:
                a += 1
            else:
                return a + 1
        return a + 1
