# Runtime 186 ms Beats 58.17%
# Memory 15.5 MB Beats 66.39%


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return len(nums)

        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i])
                i -= 1
            i += 1
        return len(nums)
