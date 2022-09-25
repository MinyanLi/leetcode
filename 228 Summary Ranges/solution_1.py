class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) < 1:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        else:
            i = 0
            group = []
            while i < len(nums)-1:
                s = [nums[i]]
                n = 0
                while n < (len(nums) -i-1):
                    if nums[i+n] == nums[i+n+1]-1:
                        s.append(nums[i+n+1])
                        n +=1
                    else:
                        break
                group.append(s)
                i = i + n + 1
            if nums[-2] != nums[-1] - 1:
                group.append([nums[-1]])

        result = []
        for i in group:
            if len(i)> 1:
                result.append(f"{i[0]}->{i[-1]}")
            else:
                result.append(f"{i[0]}")
                
        return result
            
