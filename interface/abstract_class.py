import abc

#This is my abstract class, aka Interface
class MyABC(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def do_something(self,value):
        """Req Method"""

    @property
    @abc.abstractmethod
    def x(self):
        """Required property"""
        #This above is read only property

    @x.setter
    @abc.abstractmethod
    def x(self,value):
        pass

    @x.deleter
    @abc.abstractmethod
    def x(self):
        pass


#Lets implement the interface
class MyClass(MyABC):
    def __init__(self):
        self._x = None

    def do_something(self,value):# Does not enforce the params
        print(value)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
        print('Deleted X')


mc = MyClass()
mc.do_something(mc.x)
mc.x = 'This is X'
mc.do_something(mc.x)
del mc.x
