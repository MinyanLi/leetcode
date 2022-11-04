class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        # list unique item in the list deck
        uni = list(set(deck))
        count = []

        if len(deck) == 1:
            return False    # only one card can not be divided into different groups

        for i in range(len(uni)):
            count.append(deck.count(uni[i]))   # count item incidence in the deck
        unicount = list(set(count))  # unique frequency 


        for i in range(2,len(deck)+1):  # just to make sure to have number range which can cover prime numbers for division of groups
            s = 0
            for j in range(len(unicount)):
                if unicount[j] % i == 0:    # if all the frequency can be devided by the same prime number
                    s = s + 1
            if s == len(unicount):
                return True
        return False
