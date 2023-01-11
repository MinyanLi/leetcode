# max length  O(n)
# Runtime 772 ms  Memory 27.4 MB

class Solution:
    def maxArea(self, height):
        list_len = len(height)
        if list_len == 0:
            return 0
        l = 0
        r = list_len - 1
        max_area = 0
        while l != r:
            area = (r - l) * min(height[l], height[r])
            if area > max_area:
                max_area = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

h = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(h))
