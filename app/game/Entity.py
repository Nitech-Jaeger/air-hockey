from abc import ABC,abstractmethod
import random


class Entity(ABC):
    def __init__(self, size, xposition, yposition, xspeed, yspeed):
        self._SIZE = size;    
        self._xposition = xposition
        self._yposition = yposition
        self._xspeed = xspeed
        self._yspeed = yspeed
        self.__ID = random.randint(1, 1e9)
    
    def get_position(self):
        return (self._xposition, self._yposition)
    
    def set_position(self, position):
        self._xposition = position[0]
        self._yposition = position[1]

        return 
    
    def get_id(self):
        return self.__ID
        
    
    def get_speed(self):
        return (self._xspeed, self._yspeed)

    def set_speed(self,speed):
        self._xspeed = speed[0]
        self._yspeed = speed[1]
    
    def get_size(self):
        return (self._SIZE)
    
    @abstractmethod
    def move(self):
        pass
        
