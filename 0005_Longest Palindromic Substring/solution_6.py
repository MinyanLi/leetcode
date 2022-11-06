# Runtime 1799 ms Beats 48.54%
# Memory 14.2 MB Beats 19.34%

# similar as solution 5 but without repeat calculating symetric
# https://en.wikipedia.org/wiki/Longest_palindromic_substring #Manacher's_algorithm


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
        # len(new_list) = 2* len(old_list) + 1
        s = list(s)
        for i in range(0, 2 * len(s) + 1, 2):
            s.insert(i, "|")

        radius_array = list(len(s)*"N")



        center = 0
        while center < len(s):
            radius = expand_center(s, center)
            radius_array[center] = radius
            oldcenter = center
            oldradius = radius
            radius = 0
            while center <= oldcenter + oldradius:
                # Because Center lies inside the old palindrome and every character inside a palindrome has a "mirrored" character reflected across its center, we can use the data that was precomputed for the Center's mirrored point. 
                mirrored_center = oldcenter - (center - oldcenter)
                max_mirrored_radius = oldcenter + oldradius - center
                if radius_array[mirrored_center] < max_mirrored_radius:
                    radius_array[center] = radius_array[mirrored_center]
                    center += 1
                elif radius_array[mirrored_center] > max_mirrored_radius:
                    radius_array[center] = max_mirrored_radius
                    center += 1
                else:
                    radius = max_mirrored_radius
                    break
            center += 1

        max_radius = max(radius_array)

        center = radius_array.index(max_radius)

        start = center - max_radius
        end = center + max_radius

        sub = s[start : end + 1]

        for i in range(max_radius + 1):
            sub.pop(i)
        
        sub = "".join(sub)


        return sub
