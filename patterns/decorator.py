# The decorator pattern is used widely within Python
# Anything that begins with '@' is a Python decorator

# we may write our own decorator function
def showArgs(func): # whichever function we decorate will be passed in as an argument
    '''This function may be used as a decorator for any other function
    It will reveal all the positional arguemtns and keyword argument'''
    def newFunc(*args, **kwargs): # * and ** will unpack the collections
        '''expose the args/kwargs'''
        print(f'''Running a function called {func.__name__}
The positional arguments are {args}
The keyword arguments are {kwargs}''')
        # remember to call the original function
        return func(*args, **kwargs)
    return newFunc # we do not invoke the new function

@showArgs # we apply our decorator like this
def squares(m ,n):
    '''return a list of the square integers between m and n'''
    s = []
    for i in range(m,n):
        s.append(i*i)
    return s
@showArgs
def otherFn(x,y,z):
    '''multiple x y and z'''
    return x*y*z


if __name__ == '__main__':
    # the following code only executes when we run this module directly (not via import)
    result = squares(1, 11) # here we use all positional arguments
    print(result)
    r2 = squares(m=-10, n=0) # here we use all keyword arguments
    print(r2)
    # we may apply decorators across ANY function
    o = otherFn(5,6,z=7)
    print(o)