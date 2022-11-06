# overtime

# Runtime 7355 ms Beats 7.97%
# Memory 14 MB Beats 27.82%


# function check palindromic
# check longest string whether palindromic
# check minus 1 substring
# keep minus 1 until palindromic found

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def check_palindromic(s):
            for i in range(len(s)):
                if s[i] != s[~i]:
                    return False
            return True

        sub = ""
        length = len(s)
        while length > 0:
            diff = len(s) - length
            for i in range(diff + 1):
                cur_sub = s[i: i + length]
                if check_palindromic(cur_sub):
                    return cur_sub
            length -= 1

        return sub
