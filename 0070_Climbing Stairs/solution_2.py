from functools import lru_cache

@lru_cache     # need to use cache, otherwise will calculate again and again and overtime
def f(n):
    if n > 2:
        n = f(n-1) + f(n-2)
    return n

n = f(n)
return n
