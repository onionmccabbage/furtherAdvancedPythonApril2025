def fib1(n):
    '''here is a low performance fibonacci function'''
    if n in (0,1):
        return 1
    else:
        '''recursively call tis function again'''
        return ( fib1(n-1)+fib1(n-2) )
    
if __name__ == '__main__':
    print(fib1(5))