
class Solution:
    def hasGroupsSizeX(self, deck):
      
        def gcd(a, b):
            while b:   # in python 0 == False, while b means while b != 0
              a, b = b, a % b
            return a  # get greatest common divisor 
        count = collections.Counter(deck).values()   # count incidenc of every item in deck
        return reduce(gcd, count) > 1    # The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.

      
