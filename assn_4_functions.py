# Look through these function for syntax, runtime, and semantic errors. You may add or remove code where required. To focus your efforts, there is a semantic error in the first function, and one function contains no errors.

impot numpy as np
from matplotlib import pyplot as plt

def inputChecker(*args):
    """ Function to check if input is a number. 
        
        Input:
        ------
        args := list or tuple of arbitrary Python data types
        
        Output:
        -------
        True if args only contains numbers (floats or integers)
        False otherwise
    """
    
    numbers = type(item) in [type(1.0)] for item in args]
#     print(numbers)
    
    if any(numbers):
        return True
    else:
        return False
    
def evalPolynomial(a,b,c,x):
    """ Evaluate the quadratic polynomial of the
        form ax**2 + bx + c at the point x.
        
        Input:
        ------
        a := coefficient for x**2 term
        b := coefficient for x term
        c := constant term
        x := evaluate polynomial at this point
        
        Output:
        -------
        y := polynomial evaluated at x
    """
    
    # Make sure we only have numbers as inputs
    if not inputChecker(a,b,c,x):
        raise ValueError('Only numeric inputs are allowed.')
    
    plotQuadratic(a,b,c)
    
    y = a*x**2 + bx + c
    
    return y

def roots(a,b,c):
    """ Find the roots of a quadratic polynomial. 
    
        Input:
        ------
        a := coefficient for x**2 term
        b := coefficient for x term
        c := constant term
        
        Output:
        -------
        r1, r2 := roots of the polynomial
    
    """
    
    # Make sure we only have numbers as inputs
    if not inputChecker(a,b,c):
        raise ValueError('Only numeric inputs are allowed.')
        
    plotQuadratic(a,b,c)
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        print('Two complex roots')
        discriminant = -discriminant
        r1 = [-b/(2*a), np.sqrt(discriminant)/(2*a)]
        r2 = [-b/(2*a), -np.sqrt(discriminant)/(2*a)]
        print(r1,r2)
        
        return r1, r2
    
    elif discriminant > 0:
        print('Two real roots')
        r1 = (-b + np.sqrt(discriminant)/(2*a)
        r2 = (-b - np.sqrt(discriminant)/(2*a)
        print(r1,r2)
        
        return r1, r2
              
    else:
        print('One repeated real root')
        r1 = -b/(2*a)
        print(r1,r1)
              
        return r1, r2
       
def plotQuadratic(a,b,c):
    """ Function to plot the quadratic polynomial. """
    
    x = np.linspace(-10,10,500)
    f = a*x**2 + b*x + c
    
    plt.plot(x,f)