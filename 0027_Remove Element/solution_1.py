# Runtime 36 ms Beats 92.92%
# Memory 13.8 MB Beats 63.6%

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
                i -= 1
            i += 1
        return len(nums)
