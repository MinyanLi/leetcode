# similar as solution 4


# Runtime 4561 ms Beats 16.97%
# Memory 14.2 MB Beats 19.34%

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if s == "":
            return ""

        # define a function to find max arm
        def expand_center(s, center):
            radious = 0
            while center - radious >=0 and center + radious < len(s) and s[center - radious] == s[center + radious]:
                radious += 1
            radious -= 1
            return radious

        # add "|" to s because palindrome can occur between characters
        s = list(s)
        for i in range(0, 2 * len(s) + 1, 2):
            s.insert(i, "|")

        center = 0
        radious_array = []
        while center < len(s):
            radious_array.append(expand_center(s, center))
            center += 1

        max_radious = max(radious_array)

        center = radious_array.index(max_radious)

        start = center - max_radious
        end = center + max_radious

        sub = s[start : end + 1]

        for i in range(max_radious + 1):
            sub.pop(i)
        
        sub = "".join(sub)


        return sub
