# overtime

# function check palindromic
# slide through every character and every substring

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def check_palindromic(s):
            for i in range(len(s)):
                if s[i] != s[~i]:
                    return False
            return True
                
        sub = ""
        max_len = len(sub)

        for i in range(len(s)):
            for j in range(i, len(s)):
                cur_sub = s[i:j+1]
                if check_palindromic(cur_sub):
                    if len(cur_sub) > max_len:
                        max_len = len(cur_sub)
                        sub = cur_sub
        return sub





