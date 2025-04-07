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
    '''enable a command to be executed to sell'''
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
        return self.stock.sell()

class Agent:
    '''The agent can issue commands (things to do)'''
    def __init__(self):
        self.__order_queue = [] # an empty list
    def placeOrder(self, order):
        self.__order_queue.append(order)
        # this command might be asynchronous, there may be latency
        order.execute()

def main():
    stock = StockTrade()
    buy   = BuyStock(stock)
    sell  = SellStock(stock)
    agent = Agent()
    # invoke some commands
    agent.placeOrder(buy)
    agent.placeOrder(sell)

if __name__ == '__main__':
    main()