# All design patterns are simply good ideas that have worked well before


# the constructor pattern
a = 1
class Coffee:
    def __init__(self, milk):
        self.milk = milk
    @milk # this is a property decorator
    def milk(self):
        return self.__milk
    @milk.setter
    def milk(self, new_milk):
        '''validate the values'''
        self.__milk = new_milk




# mutator pattern
l = [1,2,3]
l.append(4) # we mutate hte original constuct