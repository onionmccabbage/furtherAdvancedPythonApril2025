# Python collections:
# list:   ordinal mutable collection of any data type
# tuple:  ordinal immutable collection of any data type
# string: ordinal immutable collection of characters
# dictionary: non-ordinal mutable collection of any data type
# set: non-ordinal mutable collection of unique members of any data type
from random import randint
# functional design
def fnA(*args): # all positional arguments will be gathered into a tuple
    '''reveal all positional arguments'''
    return args

def fnB(**kwargs): # all keyword arguments will be gathered into a dictionary
    '''reveal all keyword arguments'''
    return kwargs

# pure functions guarantee the return/outcome will be predictable (deterministic)
def fnAdd(a,b):
    return a+b # there is no requirement for return - the function may just end
# impure functions have 'side effects' that are unpredictable
def fnRand():
    return randint(0,10)

if __name__ == '__main__':
    # here the arguments are ordinal - they are in a specific order
    result_a = fnA(66, 22, 'A', True, {}, 'string')
    print(result_a)
    for i in result_a:
        print(i)
    # here the arguments each have a key (the order does not matter)
    result_b = fnB(n=66, v=22, l='A', b=True, s = {}, p='string')
    print(result_b)
    for (k,v) in result_b.items():
        print(k, v)