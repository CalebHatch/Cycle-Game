import pyray


class KeyboardService:
   
    def __init__(self):
        
        self._keys = {'w': pyray.KEY_W, 'a': pyray.KEY_A, 's': pyray.KEY_S, 'd': pyray.KEY_D, 'i': pyray.KEY_I,
                      'j': pyray.KEY_J, 'k': pyray.KEY_K, 'l': pyray.KEY_L}

    def press_up_key(self, key):
        
        pyray_key = self._keys[key.lower()]
        return pyray.press_up_key(pyray_key)

    def press_down_key(self, key):
       
        pyray_key = self._keys[key.lower()]
        return pyray.press_down_key(pyray_key)