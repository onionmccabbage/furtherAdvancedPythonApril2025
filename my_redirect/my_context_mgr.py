import sys

class Redirect:
    '''this class will redirect output to a different stream
    Then return the original stream when done'''
    def __init__(self, new_stdout):
        '''__init__ runs ONCE whenever this class is instantiated'''
        self.new_stdout = new_stdout
    def __enter__(self):
        '''__enter__ will run every time an instance is used'''
        self.orig_stdout = sys.stdout # make a note of the current standard output
        sys.stdout = self.new_stdout
    def __exit__(self, exc_type, exc_value, exc_traceback):
        '''__exit__ runs every time an instance completes being used'''
        sys.stdout = self.orig_stdout # put things back how they were
    def __del__(self):
        '''this runs after everything else, when the instance is no longer required'''

def main():
    my_text = 'this will redirect to a file instead of the console'
    fout = open('my_log.txt', 'at') # we now have a file access object
    r = Redirect(fout) # we now have an instance of our class - __init__ will run once
    # now any time we need ot redirect we use our instance
    with r:
        print(my_text)
    fout.close() # good idea to tidy up
    print('back to console')


if __name__ == '__main__':
    main()