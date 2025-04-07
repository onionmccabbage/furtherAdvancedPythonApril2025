# we may need to manufacture related entities
# Here we will manufacture creatures

from abc import ABCMeta, abstractmethod

# we may declare an abstract class
class Animal(metaclass=ABCMeta):
    '''This abstract class contains no implmentation'''
    @abstractmethod
    def make_noise(self):
        pass

# we my then use this sbstrct class to create concrete implementations
class Dog(Animal): # this class inherits from our abstract class
    def make_noise(self):
        return 'woof'
class Cat(Animal):
    def make_noise(self):
        return 'miaow'
class Lion(Animal):
    def make_noise(self):
        return 'roar'
class Bat(Animal):
    def make_noise(self):
        return '______'
    

    