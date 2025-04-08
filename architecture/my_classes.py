import abc
# or....
# from abc import ABCMeta

# Unless we do otherwise, every class will inherit from 'object'
class Planar(metaclass=abc.ABCMeta):
# class Planar(metaclass=ABCMeta):
    __slots__ = ('__x', '__y') # NB ___slots__ must appear in every step of the inheritance chain
    def __init__(self):
        pass
    @abc.abstractmethod
    def hypot(self):
        pass

class Point(Planar):
    '''A 2d-point defined by x and y'''
    __slots__ = ('__x', '__y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def x(self):
        return self.__x # __x is 'name mangled' makes it almost impossible to access outside thsi class
    @x.setter
    def x(self, new_x):
        '''validate x as int or float'''
        if type(new_x) in (int, float):
            self.__x = new_x
        else:
            raise TypeError('x must be numeric')
    @property
    def y(self):
        return self.__y 
    @y.setter
    def y(self, new_y):
        '''validate y as int or float'''
        if type(new_y) in (int, float):
            self.__y = new_y
        else:
            raise TypeError('y must be numeric')
    def hypot(self):
        '''derive the hypotenuse from x and y'''
        h = (self.x**2 + self.y**2)**0.5 # NB here we call te getter-mrthod for __x and __y
        return h
    def __str__(self):
        '''override the built in __str__ to customize print for this class'''
        return f'Point at x:{self.x} y:{self.y}'
    def __repr__(self): # also used in Jupyter
        '''override the built-in __repr__ to customize representation of this class'''
        return f'Point at x:{self.x} y:{self.y}'


if __name__ == '__main__':
    p = Point(3,4)
    print(p, p.hypot()) # 5.0
    # add an arbitrary property to p
    p.__w = 'oops'

    try:
        p_err = Point('3', '4')
    except TypeError as err:
        print(f'Problem: {err}')
    except Exception as err:
        print(f'Unexpected problem: {err}')
    finally:
        print('The finally block always runs') # good place to tidy up