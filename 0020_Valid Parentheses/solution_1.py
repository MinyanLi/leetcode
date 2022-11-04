# Runtime 87 ms Beats 5.8%
# Memory 13.8 MB Beats 72.12%

class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            if "()" in s:
                s = s.replace("()", "")
            elif "{}" in s:
                s = s.replace("{}", "")
            elif "[]" in s:
                s = s.replace("[]", "")
            elif s == "":
                return True
            else:
                return False
