from threading import Thread
import time

# normal function
def standardFn():
    '''we will invoke this as a normal thread'''
    print('standard starting')
    time.sleep(5)
    print('standard done')

# daemon function
def daemonFn():
    '''we will invoke this as a daemon thread'''
    print('daemon starting')
    while True:
        time.sleep(0.5)
        print('heartbeat...')
    print('daemon done')

if __name__ == '__main__':
    standardt = Thread(target=standardFn)
    standardt.setDaemon(True)
    daemont   = Thread(target=daemonFn, daemon=True) # keep running until main htread terminates
    standardt.start()
    daemont.start()
    standardt.join()