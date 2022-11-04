
        

# make sure keep prompting until input is int
def get_int():
    n = input("Enter an int: ")
    try:
        m = int(n)
        if m == 0:
            return(get_int())
        elif m > 10000:
            return(get_int())
        else:            
            return m
    except ValueError:
        print("I need an integer to continue.")
        return(get_int())

# input    
n = get_int()


# output array
answer = []

# generation of output
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        answer.append("FizzBuzz")
    elif i % 3 == 0:
        answer.append("Fizz")
    elif i % 5 == 0:
        answer.append("Buzz")
    else:
        answer.append(i)

print(answer)
