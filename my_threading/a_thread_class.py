from threading import Thread
import random
import time

class MyClass():
    '''To call a class as a thread we override the built in __call__ method'''
    def __call__(self, n):
        '''sleep several times for a random period (emulate a long-running set of steps)'''
        for i in range(0,6):
            print(f'{n} is sleeping...')
            time.sleep(random.random()*0.1) # up to a tenth of a second

def main():
    '''invoke the class on new thread(s)'''
    c1 = MyClass()
    # we need a thread instance
    t1 = Thread(target=c1, args=(1,)) # NB a one-member tuple MUST have trailing comma
    t2 = Thread(target=c1, args=(2,))
    # we can run more than one additional thread concurrently
    t1.start() # invoke the __call__ method of the class instance
    t2.start()
    t1.join() # pause the main thread until t1 (re)joins
    t2.join()
    print('main thread...')

    # it's a good idea to tidy up
    # check about stopping redundant threads


if __name__ == '__main__':
    main()

