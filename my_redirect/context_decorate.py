# in Pyhton 3.8 and above we have a context manager built in
from contextlib import contextmanager
import sys

@contextmanager
def outputRedirect(newOutputStream):
    '''redirect to a new output context'''
    old_sto = sys.stdout
    sys.stdout = newOutputStream
    yield # our function will yield the next available context stream to be written
    sys.stdout = old_sto # put things back how they were

def main():
    '''exercise the code - check it works as expected'''
    print('using the normal context')
    with open('my_log.txt', 'at') as fobj:
        with outputRedirect(fobj):
            print('redirected output')
    print('back to the original output stream')

if __name__ == '__main__':
    main()