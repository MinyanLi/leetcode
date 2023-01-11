# brute force  O(n^2)
# Time Limit Exceeded

class Solution:
    def maxArea(self, height):
        list_len = len(height)
        i = 0
        j = 1
        max_area = 0
        while i < list_len - 1:
            while j < list_len:
                area = (j - i) * min(height[i], height[j])
                if area > max_area:
                    max_area = area
                j += 1
            i += 1
            j = i + 1

        return max_area

h = [1,8,6,2,5,4,8,3,7]
h = [1,1]
print(Solution().maxArea(h))
