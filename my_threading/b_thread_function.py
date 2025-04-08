from threading import Thread
import random
import time

def myFn(n):
    for i in range(0,6):
        print(f'{n} is sleeping')
        time.sleep( random.random()*0.1 )

def main():
    '''invoke the function on additional threads'''
    t1 = Thread(target=myFn, args=(1,))
    t2 = Thread(target=myFn, args=(2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()