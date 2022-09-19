
from collections import Counter  
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            if ransomNote.count(i)>magazine.count(i):
                return False
        return True
      
      
'''
counter = Counter(['a', 'a', 'b'])
print(counter)  
# Counter({'a': 2, 'b': 1})
'''


'''
s = "hellobye"
print(set(s))
#{'b', 'o', 'e', 'h', 'l', 'y'}
'''


'''
s = "hellobye"
print(s.count("e"))
# 2
'''
