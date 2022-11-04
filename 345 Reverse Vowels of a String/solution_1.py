# Runtime 1733 ms Beats 5.1%
# Memory 15.6 MB Beats 20.88%

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowels_in_s = []
        # collect all the vowels
        for i in range(len(s)):
            for j in range(len(vowels)):
                if s[i] == vowels[j]:
                    vowels_in_s.append(s[i])

        # reverse list of vowels
        reverse_vowels = []
        for i in range(len(vowels_in_s)):
            reverse_vowels.append(vowels_in_s[~i])

        # put reverse vowels in s
        s_list = list(s)
        a = 0
        for i in range(len(s)):
            for j in range(len(vowels)):
                if s[i] == vowels[j]:
                    s_list.pop(i)
                    s_list.insert(i, reverse_vowels[a])
                    a += 1

        s_reverse_vowels = ""
        for i in range(len(s)):
            s_reverse_vowels = s_reverse_vowels + s_list[i]

        return s_reverse_vowels
