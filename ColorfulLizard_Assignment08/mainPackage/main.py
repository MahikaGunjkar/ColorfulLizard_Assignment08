# Name: Mahika Gunjkar, Nandini Agrawal, Ishani Roy Chowdhury
# email:  gunjkamg@mail.uc.edu, Agarwand@mail.uc.edu, roychoii@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   10/31/2024
# Course #/Section:  4010- 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Team assignment based on real-life example like home techonology. We wrote code to correlate a few home techonologies together

# Brief Description of what this module does. This module is the main module and talks about all the prints statements and joints that are required.
# Citations:
# Anything else that's relevant:

 #main.py
from lightPackage.light import *
from speakerPackage.speaker import *


if __name__ == "__main__":
   
    try:
        # Instantiate each class
        light = SmartLight(brightness=70, color="Cool White")
        speaker = SmartSpeaker(volume=7, track_name="Chill Vibes")

        # Demonstrate functionality for SmartLight
        print(light)                # Calls __str__
        light.toggle()              # Turn on/off the light
        light.change_color("Blue")  # Change color
        light.brightness = 80       # Adjust brightness
        print(light)

        # Demonstrate functionality for SmartSpeaker
        print(speaker)                     # Calls __str__
        speaker.play_music("Jazz Beats")   # Change track
        speaker.change_volume(5)           # Adjust volume
        print(speaker)

    except Exception as e:
        print(f"An error occurred: {e}")
