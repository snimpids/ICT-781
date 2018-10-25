""" Introductory Python Module """

import random as rd

def gamesDict(titles, years, publishers):
    """ Makes a dictionary of games based on  
        user-supplied titles, years, and publishers.
    """ 
    
    # Check lengths of inputs.
    if len(titles) != len(years) != len(publishers):
        M = max([len(titles),len(years),len(publishers)])
        
        # If the inputs have different lengths, fill out the shorter input lists with None.
        for i in [titles,years,publishers]:
            for j in range(len(i),M):
                i.append(None)
                
    return {title: info for title, info in zip(titles,zip(titles,years,publishers))} 

def changeString(string):
    """ Performs various transformations on input string. 
        The output is a list of different versions of the
        string.
    """
    
    # Change all 'e' letters to 'i', then capitalize all 'a' letters.
    stringe = string.replace('e','i')
    stringe = [letter.upper() if letter == 'a' else letter for letter in stringe]
    stringe = ''.join(stringe)
    
    # Change all instances of 'you','me','him','her' to 'Scooby'.
    stringL = string.split()
    to_scoobify = ['you','me','him','her']
    string_scooby = ['Scooby' if word in to_scoobify else word for word in stringL]
    string_scooby = ' '.join(string_scooby)
    
    return [stringe,string_scooby]

def multiplesThreeFive(lower_bound, upper_bound):
    """ Function to add up multiples of 3 and 5 between the supplied bounds. """
    
    # If the lower bound is bigger than the upper bound, switch them.
    if lower_bound > upper_bound:
        lower_bound, upper_bound = upper_bound, lower_bound
        
    # There's nothing to calculate if the bounds are equal.
    if int(lower_bound) is int(upper_bound):
        raise ValueError('There is no interval between {0} and {1}.'.format(lower_bound,upper_bound))
        
    # Convert bounds to integers.
    lower_bound, upper_bound = int(lower_bound), int(upper_bound)
    
    multiples_of_3_or_5 = [i for i in range(lower_bound,upper_bound+1) if i % 3 == 0 or i % 5 == 0]
    return sum(multiples_of_3_or_5)

def factorial(n):
    """ The factorial function. """
        
    total = 1
    for i in range(1,n+1):
        total *= i
        
    return total

def factorialRecursive(n):
    """ The recursive factorial function. """
    total = n
    
    if n > 1:
        total *= factorialRecursive(n-1)
    
    return total 

def selectNames(names):
    """ Function to randomly select names from the list of names. """
    giftees = rd.sample(names, len(names))
    result = list(zip(names, giftees))
    
    return result

def checkNames(result):
    """ Check if any names are duplicated. """
    if any(result[i][0] is result[i][1] for i in range(len(result))):
        return True
    else:
        return False

def nameDraw(names):
    """ Performs the random name draw. """
    result = selectNames(names)
    
    # Make sure there's nobody buying for themselves.
    while checkNames(result):
        result = selectNames(names)
    
    return result

def paragraphDecorator(func):
    """ Place output inside an HTML paragraph. """
    
    def wrapper(text):
        return '<p> {} </p>'.format(func(text))
    
    return wrapper

@paragraphDecorator
def printFunc(text):
    """ Prints out string argument. """
    
    return 'User input the following: {}'.format(text)

def printCandidates(candidates, *args, **kwargs):
    """ Print out election candidates. """
    
    # Ensure candidates argument is a list.
    if type(candidates) is not type([]):
        candidates = [candidates]
    
    for candidate in candidates:
        print(candidate)
        
    for arg in args:
        print(arg)
        
    for key in kwargs:
        print(key,':',kwargs[key])
        
    if 'total_votes' in kwargs:
        print(kwargs['total_votes']*80)