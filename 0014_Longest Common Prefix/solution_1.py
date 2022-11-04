# Runtime 41 ms Beats 87.9%
# Memory 13.8 MB Beats 88.35%

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        prefix_idx = 0
        while True:
            for i in range(len(strs)):
                try:
                    if strs[0][prefix_idx] != strs[i][prefix_idx]:
                        return common
                except IndexError:
                    return common
            common = common + strs[0][prefix_idx]
            prefix_idx += 1
        return common
