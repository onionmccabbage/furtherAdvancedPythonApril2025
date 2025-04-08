# Here we havea ticket selling engine
# severla tichet selling instances will sell tickets from a global pool

import threading
import time
import random
# timeit tries to avoid non-python stuff
import timeit # this is the most accurate way to measure how long Python takes to run

# here is a global variable
ticketsAvailable = 1024

class TicketSeller(threading.Thread):
    '''imitate random time between sales'''
    ticketsSold = 0 # class member
    def __init__(self, sem):
        threading.Thread.__init__(self)
        self.sem = sem # each of our threads has access to the SAME lock
        print(f'Ticket seller starts selling tickets')
    def run(self):
        global ticketsAvailable   # or access a db, a file, an API
        running = True
        while running:
            self.randomDelay()
            self.sem.acquire() # exclusively access shared resources
            if ticketsAvailable <=0:
                running = False # stop running!
            else:
                ticketsAvailable -= 1
                self.ticketsSold += 1
                # print(f'Sold a ticket {ticketsAvailable} remaining')
            self.sem.release() # mke global assets avaialble to other threads
        print(f'Sold {self.ticketsSold}')
    def randomDelay(self):
        time.sleep(random.randint(0,4)/4) # 0, 0.25, 0.5, 0.75

# NB with all code, including threads, i/o bound operations will s-l-o-w the code

if __name__ == '__main__':
    sem = threading.Semaphore(4) # we may choose how many concurrent threads may access our data
    sellers_list = []
    # we may use a thread lock to make threads safe (nique access to global assets)
    start = timeit.default_timer()
    for _ in range(0, 64):
        seller = TicketSeller(sem)
        sellers_list.append(seller)
        seller.start() # each thread is invoked
    for _ in sellers_list:
        _.join()
    end = timeit.default_timer()
    print(f'total operatiom took {end-start}')
