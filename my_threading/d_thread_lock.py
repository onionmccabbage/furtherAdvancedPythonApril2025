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
    def __init__(self):
        threading.Thread.__init__()
        print(f'Ticket seller starts selling tickets')
    def run(self):
        global ticketsAvailable   # or access a db, a file, an API
        running = True
        while running:
            self.randomDelay()
            if ticketsAvailable <=0:
                running = False # stop running!
            else:
                ticketsAvailable -= 1
                self.ticketsSold += 1
                print(f'Sold a ticket {ticketsAvailable} remaining')
        print(f'Sold {self.ticketsSold}')
    def randomDelay():
        time.sleep(random.randint(0,4)/4) # 0, 0.25, 0.5, 0.75


