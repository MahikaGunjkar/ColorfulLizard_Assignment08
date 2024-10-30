# Name: {required}
# email:  {required}
# Assignment Number: Assignment nn  {required}
# Due Date:   {required}
# Course #/Section:   {required}
# Semester/Year:   {required}
# Brief Description of the assignment:  {required}

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations:
# Anything else that's relevant:

 
#light.py

class SmartLight:
    def _init_(self, brightness=50, color="Warm White", is_on=False):
        self._brightness = brightness
        self._color = color
        self._is_on = is_on

    def _str_(self):
        return f"SmartLight(brightness={self._brightness}, color={self._color}, is_on={self._is_on})"

    def _repr_(self):
        return f"SmartLight({self._brightness}, '{self._color}', {self._is_on})"

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        if 0 <= value <= 100:
            self._brightness = value
        else:
            print("Brightness should be between 0 and 100")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def toggle(self):
        self._is_on = not self._is_on
        state = "on" if self._is_on else "off"
        print(f"The light is now {state}.")

    def change_color(self, new_color):
        self.color = new_color
        print(f"The light color is now {self.color}.")
