from threading import Thread, Event
import time

event = Event() # a global asset
def myFn():
    '''each thread has exclusive access to the Python process'''
    global event
    print(f'Waiting for a thread event')
    event.wait()



if __name__ == '__main__':
    # exercise the code