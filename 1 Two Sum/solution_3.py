# 136 ms	15.4 MB
# put the target - num item subtraction result in to a dictionary with index
# look for matching (less searching)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for index in range(len(nums)):
            if nums[index] in table:
                return [table[nums[index]], index]
            table[target - nums[index]] = index    # table = { (target - nums[index]): index}
