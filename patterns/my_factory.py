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
    
class CreatureFactory:
    '''This is a single-point-of-access to manufacture any type of creature avilable'''
    def make_sound(self, obj):
        # e.g. cat, lion etc
        return eval(obj)().make_noise()    

if __name__ == '__main__':
    cf = CreatureFactory() # an instance of our factory
    creature = input('Which creature: ')
    noise = cf.make_sound(creature) 
    print(f'The {creature} says {noise}')
