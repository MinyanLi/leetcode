# overtime

# create a reverse string
# compare string and reverse string
# collect matching strings into dictionary
# check the longest substring whether palidrome

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def check_palindromic(s):
            for i in range(len(s)):
                if s[i] != s[~i]:
                    return False
            return True

        s = list(s)
        reverse_s = []
        for i in range(len(s)):
            reverse_s.append(s[~i])
        
        # compare s and reverse_s, collect match substrings into a list

        sub_collect = []
        for i in range(len(s)):
            temp_i = i
            for j in range(len(reverse_s)):
                temp_j = j
                sub = []
                while i < len(s) and j < len(reverse_s):
                    if s[i] == reverse_s[j]:
                        sub.append(s[i])
                        i += 1
                        j += 1
                    else:
                        i = temp_i
                        j = temp_j + 1
                        break
                if sub != []:
                    sub_collect.append(sub)       


        # put substrings and length into dictionary
        dict = {}
        for i in sub_collect:
            i = "".join(i)
            dict[i] = len(i)

        sorted_dict = sorted(dict.items(), key= lambda x:x[1], reverse = True)

        for i in sorted_dict:
            if check_palindromic(i[0]):
                return i[0]

        return ""
