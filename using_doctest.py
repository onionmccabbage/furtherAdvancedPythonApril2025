import doctest

def fn(a,b):
    '''
    >>> fn(3,4)
    7
    '''
    return a+b

if __name__ == '__main__':
    doctest.testmod()