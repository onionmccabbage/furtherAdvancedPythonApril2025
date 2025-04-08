from threading import Thread
import random
import time

class MyClass(Thread): # we inherit everything from the Thread class
    '''to use a class inheriting from thread, implement a run method'''
    def __init__(self, n):
        Thread.__init__(self) # easier to call Thread.__init__ not super().__init()
        self.n = n # we could use get/set methods
    def run(self):
        for i in range(0,6):
            print(f'{self.n} is sleeping')
            time.sleep(random.random()*0.1)

def main():
    '''invoke the class as a thread'''
    # to work with many threads, use loops
    thread_list = []
    for _ in range(0,8):
        thread_list.append( MyClass(_) )
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    print('back on the main thread')


if __name__ == '__main__':
    main()