import timeit
from functools import reduce
from memory_profiler import profile
# we may atain a profile of any code using cProfile
# python -m cProfile -o profile_output fib.py


# we can only use @profile to decorate functions and classes
@profile
def fib1(n):
    '''here is a low performance fibonacci function'''
    if n in (0,1):
        return 1
    else:
        '''recursively call tis function again'''
        return ( fib1(n-1)+fib1(n-2) )

def fib2(n):
    '''a more performant solution''' 
    sequence = (0,1)
    for _ in range(2, n+2):
        # NB we do not mutate the tuple
        sequence += (reduce( lambda a,b: a+b, sequence[-2:] ),)
    return sequence[-1] # return the last member of the sequence

def main():
    start = timeit.default_timer()
    print(fib1(28)) # 0.14 sec for fib1, 0.00013 for fib2
    end=timeit.default_timer()
    print(f'total time: {end-start}')

if __name__ == '__main__':
    main()