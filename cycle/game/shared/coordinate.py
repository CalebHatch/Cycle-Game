class Coordinate:
    # Is able to place the players' cycles where they are supposed to be.
    
    def __init__(self, x, y):

        self._x = x
        self._y = y

    def add(self, other):
       
        x = self._x + other.get_x()
        y = self._y + other.get_y()

        return Coordinate(x, y)

    def get_x(self):
       
        return self._x

    def get_y(self):
        
        return self._y

    def reverse(self):
        
        new_x = self._x * -1
        new_y = self._y * -1

        return Coordinate(new_x, new_y)
