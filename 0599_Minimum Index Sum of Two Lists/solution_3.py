class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
      
        indices = {r:i for i, r in enumerate(list1)}  # enumerate gives an index
        
        best, ans = float('inf'), []    # floa("inf") means the large possible number
        
        for i,r in enumerate(list2):
            if r not in indices: continue  # only r in both list1 list2 will go through next
            if i + indices[r] < best:      # index sum < large possible number
                best = i + indices[r]      # will find out the min index sum
                ans = [r]
            elif i + indices[r] == best:
                ans.append(r)
        return ans
