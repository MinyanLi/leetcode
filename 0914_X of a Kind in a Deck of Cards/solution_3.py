
class Solution(object):
    def hasGroupsSizeX(self, deck):
      
        count = collections.Counter(deck)  # count item incidency
        N = len(deck)
        for X in range(2, N+1):
            if N % X == 0:   # x is possible number of groups
                if all(v % X == 0 for v in count.values()):  # all incidency can be devided into same number of groups
                    return True
        return False
