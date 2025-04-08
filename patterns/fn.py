# Python collections:
# list:   ordinal mutable collection of any data type
# tuple:  ordinal immutable collection of any data type
# string: ordinal immutable collection of characters
# dictionary: non-ordinal mutable collection of any data type
# set: non-ordinal mutable collection of unique members of any data type

# functional design
def fnA(*args): # all positional arguments will be gathered into a tuple
    '''reveal all positional arguments'''
    return args

def fnB(**kwargs): # all keyword arguments will be gathered into a dictionary
    '''reveal all keyword arguments'''
    return kwargs




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