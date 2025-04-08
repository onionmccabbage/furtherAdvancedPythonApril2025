# Here we havea ticket selling engine
# severla tichet selling instances will sell tickets from a global pool

import threading
import time
import random

# here is a global variable
ticketsAvailable = 100

class TicketSeller(threading.Thread):
    '''imitate random time between sales'''
    ticketsSold = 0 # class member
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.lock = lock # each of our threads has access to the SAME lock
        print(f'Ticket seller starts selling tickets')
    def run(self):
        global ticketsAvailable   # or access a db, a file, an API
        running = True
        while running:
            self.randomDelay()
            self.lock.acquire() # exclusively access shared resources
            if ticketsAvailable <=0:
                running = False # stop running!
            else:
                ticketsAvailable -= 1
                self.ticketsSold += 1
                print(f'Sold a ticket {ticketsAvailable} remaining')
            self.lock.release() # mke global assets avaialble to other threads
        print(f'Sold {self.ticketsSold}')
    def randomDelay(self):
        time.sleep(random.randint(0,4)/4) # 0, 0.25, 0.5, 0.75

if __name__ == '__main__':
    sellers_list = []
    # we may use a thread lock to make threads safe (nique access to global assets)
    lock = threading.Lock() # we have an instance of e lock
    for _ in range(0, 4):
        seller = TicketSeller(lock)
        sellers_list.append(seller)
        seller.start() # each thread is invoked
    for _ in sellers_list:
        _.join()
