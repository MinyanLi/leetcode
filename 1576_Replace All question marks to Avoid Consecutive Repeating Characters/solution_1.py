# 77 ms	14 MB

class Solution:
    def modifyString(self, s: str) -> str:
        
        alpha = "abcdefghijklmnopqrstuvwxyz"
        
        if not "?" in s:
            return s
          
        else: # there's "?" in s
            string = ""
            if len(s) == 1:
                if s[0] == "?":
                    string = "a"
                else:  # s[0] != "?"
                    string = s[0]

            else: # len(s)>=2
                if s[0] == "?":
                    if s[1] != "?":
                        k = alpha.index(s[1])
                        alpha = alpha[:k] + alpha[k+1:]
                        # choose the first character in alphabet
                        string = string + alpha[0]
                        alpha = "abcdefghijklmnopqrstuvwxyz"
                    else:
                        string = "a"
                else:
                    string = string + s[0]

                for i in range(1,len(s)-1):
                    if s[i] != "?":
                        string = string + s[i]
                    else:
                        if string[i-1] == s[i+1] or s[i+1] == "?":
                            j = alpha.index(string[i-1])
                            alpha = alpha[:j] + alpha[j+1:]
                            string = string + alpha[0]
                            alpha = "abcdefghijklmnopqrstuvwxyz" 
                        else:
                            m = alpha.index(string[i-1])
                            alpha = alpha[:m] + alpha[m+1:]
                            p = alpha.index(s[i+1])
                            alpha = alpha[:p] + alpha[p+1:]
                            string = string + alpha[0]    
                            alpha = "abcdefghijklmnopqrstuvwxyz"   


                if s[-1] == "?":
                    b = alpha.index(string[-1])
                    alpha = alpha[:b] + alpha[b+1:]
                    string = string + alpha[0] 
                    alpha = "abcdefghijklmnopqrstuvwxyz"
                else:
                    string = string + s[-1]


            return string
            

        
        
