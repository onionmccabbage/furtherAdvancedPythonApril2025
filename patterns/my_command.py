from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass  # we never write implementation code within an abstract class

class StockTrade:
    '''low-level buy and sell operations'''
    def buy(self):
        print('buy stocks')
    def sell(self):
        print('sell stocks')

class BuyStock(Order):
    '''enable a command to be executed to buy'''
    def __init__(self, stock):
        self.stock = stock
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, new_stock):
        if type(new_stock) == StockTrade:
            self.__stock = new_stock
        else:
            raise TypeError('Missing required stock trade instance')
    def execute(self):
        return self.stock.buy()

class SellStock(Order):
    pass

class Agent:
    pass

def main():
    pass

if __name__ == '__main__':
    main()