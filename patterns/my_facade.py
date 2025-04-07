# we need to bring together different capabilities

class Coder:
    '''writes code'''
    def __init__(self):
        print('write some code')
    def __is_available(self):
        return True # we may have logic to check here
    def book_time(self):
        if self.__is_available():
            print('coder has been booked')

class Tester:
    '''configures tests'''
    def __init__(self):
        print('preparing some tests')
    def testing(self):
        print('tests are in place for due diligence')

class Technician:
    '''do technical stuff'''
    def __init__(self):
        print('preparing equipment for the team')
    def doStuff(self):
        print('network, machines, cloud, ML all in place')

class Artisan:
    '''designing capabilities'''
    def __init__(self):
        print('designing things')
    def make_prototype(self):
        print('wireframes are ready')

class Manager:
    '''the manager is the facade for all the team mebers'''
    def __init__(self):
        print('Manager says I can arrange the team')
    def arrange(self):
        '''The facade provides instances of all the other subsystems/microservices'''
        self.coder      = Coder()
        self.tester     = Tester()
        self.technician = Technician()
        self. artisan   = Artisan()
        # we may call on additional assets...
        # Next we invoke methods of these subsystems
        self.coder.book_time()
        self.tester.testing()
        self.technician.doStuff()
        self.artisan.make_prototype()

if __name__ == '__main__':
    manager = Manager()
    manager.arrange()
