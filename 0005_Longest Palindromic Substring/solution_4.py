# Runtime 679 ms Beats 85.66%
# Memory 14.1 MB Beats 27.82%

# slide every center to find the longest palindrome
# center can be a single character if the palindrome is odd
# center can be between two same characters if the palindrome is even

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand_center(s, left, right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        if s == "":
            return ""

        start = 0
        end = 0
        i = 0
        while i < len(s):
            print("i:", i)
            len_odd = expand_center(s, i, i)
            print("odd:",len_odd)
            len_even = expand_center(s, i, i + 1)
            print("even:",len_even)
            len_max = max(len_odd, len_even)
            print("max:", len_max)
            if len_max > end - start:
                start = i -(len_max -1)//2
                end = i + len_max // 2
            i += 1 

        return s[start: end + 1]

