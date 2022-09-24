class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        enums = enumerate(nums)
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in nums:
                j = nums.index(rest)
                if i != j:
                    return i, j
