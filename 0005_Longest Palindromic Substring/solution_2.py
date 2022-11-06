# overtime

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
