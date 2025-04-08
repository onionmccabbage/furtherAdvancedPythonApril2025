# functional design
def fnA(*args):
    '''reveal all positional arguments'''
    return args

def fnB(**kwargs):
    '''reveal all keyword arguments'''
    return kwargs

if __name__ == '__main__':
    # here the arguments are ordinal - they are in a specific order
    result_a = fnA(66, 22, 'A', True, {}, 'string')
    print(result_a)
    # here the arguments each have a key (the order does not matter)
    result_b = fnB(n=66, v=22, l='A', b=True, s = {}, p='string')
    print(result_b)