from abc import ABC,abstractmethod

class Entity(ABC):
    def __init__(self,size,xposition,yposition,xspeed,yspeed):
        self._SIZE = size;    
        self._xposition = xposition
        self._yposition = yposition
        self._xspeed = xspeed
        self._yspeed = yspeed
    
    def get_position(self):
        return (self._xposition,self._yposition)
    
    def set_position(self,position):
        self._xposition = position[0]
        self._yposition = position[1]
    
    def get_speed(self):
        return (self._xspeed,self._yspeed)
    
    def get_size(self):
        return (self._SIZE)
    
    @abstractmethod
    def move(self):
        pass
        
