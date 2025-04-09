import multiprocessing
import os
import time
import timeit

def myProc(n):
    '''run this on a separate process'''
    print(f'{n} Running in a separate process {os.getpid()}')
    time.sleep(2)

if __name__ == '__main__':
    start = timeit.default_timer()
    print(f'The main process is running on {os.getpid()}')
    # a list to hold our process instances
    pl=[]
    # a loop (or comprehension) to start several processes
    for p in range(64):
        proc = multiprocessing.Process(target=myProc, args=(p,))
        proc.start()
        pl.append(proc)
    # a loop to join
    d = [p.join for p in pl]
    # pA = multiprocessing.Process(target=myProc, args=(1,))
    # pB = multiprocessing.Process(target=myProc, args=(2,))
    # pA.start()
    # pB.start()
    # # the main proces carries on unless we tell it to wait for the other proceses
    # pA.join()
    # pB.join()
    end = timeit.default_timer()
    print(f'Total time: {end-start}')
