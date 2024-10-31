# Name: Mahika Gunjkar, Nandini Agrawal, Ishani Roy Chowdhury
# email:  gunjkamg@mail.uc.edu, Agarwand@mail.uc.edu, roychoii@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   10/31/2024
# Course #/Section:  4010- 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Team assignment based on real-life example like home techonology. We wrote code to correlate a few home techonologies together
# Brief Description of what this module does. This module defines a SmartLight class representing a smart light device with customizable settings. The smartLight has Toggle Power which used to turn the light on or off, 
#Adjust brightness to Set the level within a range of 0 to 100, Change the color to Modify the color of the light. This module helps in the creation and the control of the smart light objects and helps to make it ideal for use in home automation systems
# Citations:
# Anything else that's relevant:
 
#light.py

class SmartLight:
    def __init__(self, brightness=50, color="Warm White", is_on=False):
        self._brightness = brightness
        self._color = color
        self._is_on = is_on

    def __str__(self):
        return f"SmartLight(brightness={self._brightness}, color={self._color}, is_on={self._is_on})"

    def __repr__(self):
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
