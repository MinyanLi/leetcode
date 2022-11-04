# 11ms

class Solution:
    def isValid(self, s: str) -> bool:
      
        stack = []
        
        dict1 = {'(':')','{':'}','[':']'}
        
        for i in s:
            if i in dict1.keys():    # if i is open perenthesis
                stack.append(i)
            else:
                if len(stack) == 0:   # if s[0] is not open perenthsis
                    return False
                x = stack.pop()       # if i is not open perenthesis, if there's open perenthsis previously, pick out the last open perenthesis
                if i != dict1[x]:     # if i is close perenthesis and i is not the correspondent of the last open perenthesis
                    return False
        if len(stack)>0:
            return False
        return True
