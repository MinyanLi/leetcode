# 49ms

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        if len(s) <= numRows:
            return s
        pattern_dict = ['' for i in range(numRows)]
        mod = numRows * 2 - 2

        for ind, c in enumerate(s):
            dict_id = ind % mod
            if dict_id >= numRows:
                dict_id = mod - dict_id
            pattern_dict[dict_id] += c



        out_s = ''.join(pattern_dict)
        # out_s = ''.join([''.join(p) for p in pattern_dict])
        # for i in range(numRows):
        #     val = pattern_dict[i]
        #     for c in val:
        #         out_s += c


        return out_s
