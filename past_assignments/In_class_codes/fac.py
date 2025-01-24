
def fac(n):

    if n > 0:

        return n * fac(n-1)
    
    else:
        return 1

def fib(n):

    if n == 0:
        return 1
    
    elif n == 1:
        return 1
    
    else:
        return fib(n-1) + fib(n-2)


for i in range(10):
    #print(fib(i))
    pass



# if n == 0 then return 0
# if n > 0 return n + sum(n-1)

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
    
for i in range(10):
    print(sum(i))