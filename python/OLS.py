## OLS
## Work in Progress

def RSS(a,b,x,y):
# given two parameters and a list of x values, return y values
# assume all inputs are floats
    N = len(x)
    squaredResiduals [(y - (x*a + b))**2 for i in range(N)]
    RSS = sum(squaredResiduals)
    return RSS
    
def SGD(RSS, a_init, b_init, x, y):    
    ssA = 0.01
    ssB = 0.01
    precision = 0.0001
    a_old = a_init
    a_new = a_init + ssA
    b_old = b_init
    b_new = b_init + ssB
    # x_i = x_i-1 - alpha * fprime(x_i-1)
    while (RSS(a_old, b_old, x, y) - RSS(a_new, b_new, x, y)) < precision:
        
    
    
def OLS(x,y):
# input is two lists of floats with the x & y coordinates for some points
    try: len(x) == len(y) 
    except: Error # lookup error type

    N = len(x)
    a_init = 1
    b_init = 1
    
    RSS(a, b, x, y)