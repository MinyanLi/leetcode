class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        from collections import Counter
        
        # pop out each character to check whether the rest has same frequency
        for i in range(len(word)):
            temp = word[:i] + word[i+1:]
            print(temp)
            count = Counter(temp)
            if min(count.values()) == max(count.values()):
                return True
            else:
                continue
        
        return False
      
      
      
class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            if len(set(Counter(word[0:i] + word[i+1:]).values())) == 1:
                return True
        return False
