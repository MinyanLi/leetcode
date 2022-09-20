# Return sends a specified value back to its caller whereas Yield can produce a sequence of values. We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory. Yield is used in Python generators. A generator function is defined just like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function. 

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        for i in range(1, n+1):
            if i % 15 == 0:
                yield "FizzBuzz"
            elif i % 3 == 0:
                yield "Fizz"
            elif i % 5 == 0:
                yield "Buzz"
            else:
                yield str(i)
            
        
