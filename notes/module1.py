def normalize(data):
    """ Normalize numerical dataset based on its mean and standard deviation. 
        
        Input:
        ------
        data := Python list
        
        Output:
        -------
        (data-mean(data))/std(data)
    """
    
    import numpy as np
    
    average = np.mean(data)
    stdev = np.std(data)
    
    normalized_data = [(x-average)/stdev for x in data]
    
    return normalized_data

def build_data(columns):
    """ Build a spreadsheet-like dataset. """
    
    return {col : None for col in columns}

def factorial_recursive(n):
    """ The recursive factorial function. """
    total = n
    
    if n > 1:
        total *= factorial_recursive(n-1)
    
    return total

def n_choose_k(n,k):
    """ Compute n!/(k!(n-k)!) """
    
    if k > n:
        return 0
    
    return factorial_recursive(n)/(factorial_recursive(k)*factorial_recursive(n-k))

def n_pick_k(n,k):
    """ Compute n!/(n-k)! """
    
    if k > n:
        return 0
    
    return factorial_recursive(n)/factorial_recursive(n-k)