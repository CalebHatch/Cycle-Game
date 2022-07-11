class Color:

    def __init__(self, red, green, blue, alpha=255):
        self._red = red
        self._green = green
        self._blue = blue

    def colors(self):
        return self._red, self._green, self._blue
