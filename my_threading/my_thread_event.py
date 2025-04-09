from threading import Thread, Event
import time

event = Event() # a global asset
def myFn(n):
    '''each thread has exclusive access to the Python process'''
    global event
    print(f'{n} Waiting for a thread event')
    event.wait()
    print(f'{n} Continuing after the event')


if __name__ == '__main__':
    # exercise the code
    # we need a list for our threads
    t_l = []
    for _ in range(4):
        t = Thread(target=myFn, args=(_,))
        t_l.append(t)
        t.start()
    # pause a while 
    time.sleep(4)
    event.set()