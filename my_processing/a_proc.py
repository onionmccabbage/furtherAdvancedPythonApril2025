import multiprocessing
import os

def myProc(n):
    '''run this on a separate process'''
    print(f'{n} Running in a separate process {os.getpid()}')

if __name__ == '__main__':
    print(f'The main process is running on {os.getpid()}')
    pA = multiprocessing.Process(target=myProc, args=(1,))
    pB = multiprocessing.Process(target=myProc, args=(2,))
    pA.start()
    pB.start()
