# Runtime 72 ms Beats 8.51%
# Memory 13.8 MB Beats 68.81%


class Solution:
    def equalFrequency(self, word: str) -> bool:
        l = list(set(word))
        frequency = []
        for i in range(len(l)):
            frequency.append(word.count(l[i]))
        f = list(set(frequency))
        # if all the characters are the same
        if (len(frequency) == 1):
            return True
        # if every character only occur once
        if (f == [1]):
            return True
        if (len(f) == 2):
            # if there's one character only occur once and other charaters has same frequence but not 1
            if (f[0] == 1 and frequency.count(f[0]) == 1):
                return True
            # if one character occured once more than any other characters
            if ((frequency.count(f[1]) == 1) and (f[1] - f[0] == 1)):
                return True
        return False
        
