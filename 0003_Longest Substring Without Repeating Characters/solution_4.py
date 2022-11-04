# 46ms

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      j = -1                                     # ensure j < starting index
      chars = {}                                 # putting characters(ch) with index(i) in dictionary(chars), only contian the most recent index
      ans = 0
      for i,ch in enumerate(s):                  # indexing characters(ch) in s
          if ch in chars and chars[ch] > j:      # if ch already exists in chars
              j = chars[ch]                      # put the previous index to j
              print("i", i, "ch:",ch, "j:", j)
          else:
              if ans < i-j:                      # distance of 2 same ch index
                  ans = i-j
                  print("ans", ans)
          chars[ch] = i                          # putting characters(ch) with index(i) in dictionary(chars), only contian the most recent index
