class Solution:
    def equalFrequency(self, word: str) -> bool:
        """ O(N)TS """
        v = collections.Counter(collections.Counter(word).values())
        a = len(v) == 1 and (1 in v or 1 in v.values())
        b = len(v) == 2 and (1, 1) in v.items()
        c = len(v) == 2 and (list(v)[0] + 1, 1) in v.items()
        d = len(v) == 2 and (list(v)[1] + 1, 1) in v.items()
        return a or b or c or d
