class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        import sys
        import re
        
        # constrain input length
        if len(ransomNote) == 0:
            sys.exit("Too short ransomNote")
            
        if len(magazine) > 100000:
            sys.exit("Too long magazine")
            
        if len(ransomNote) > len(magazine):
            return False
            
        # lower case English letters only
        if re.search("(?:a-z )", ransomNote):
            sys.exit("contain non lower case English letter")
        if re.search("(?:a-z )", magazine):
            sys.exit("contain non lower case English letter")
            
                     
        # if first character in string a matches any character in string b, 
        # remove first character in a and first match in b
        # count the match
        def match_and_remove(a,b):
            n = 0
            for i in range(len(b)):
                if a[0] == b[i]:
                    a = a[ 1 : ] 
                    b = b[ : i] + b[ i + 1 : ]   
                    n = n + 1
                    return a, b, n
            return a, b, n
 


        l = len(ransomNote)   # orignal lenth of str ransomNote
        n=0    # match count

        # iterater to count match
        for i in range(len(ransomNote)):
            ransomNote, magazine, d = match_and_remove(ransomNote,magazine)
            n = n + d

                    
        if n == l:
            return True
        else:
            return False
