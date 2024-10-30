
main.py
  from smart_home.light import SmartLight
from smart_home.thermostat import Thermostat
from smart_home.speaker import SmartSpeaker

if __name__ == "__main__":
  
    # Instantiate each class
    light = SmartLight(brightness=70, color="Cool White")
    thermostat = Thermostat(current_temp=21, desired_temp=23)
    speaker = SmartSpeaker(volume=7, track_name="Chill Vibes")

    # Demonstrate functionality for SmartLight
    print(light)                # Calls __str__
    light.toggle()              # Turn on/off the light
    light.change_color("Blue")  # Change color
    light.brightness = 80       # Adjust brightness
    print(light)

    # Demonstrate functionality for Thermostat
    print(thermostat)                  # Calls __str__
    thermostat.adjust_temperature(24)  # Change desired temperature
    thermostat.current_temp = 22       # Update current temperature
    print(thermostat)

    # Demonstrate functionality for SmartSpeaker
    print(speaker)                     # Calls __str__
    speaker.play_music("Jazz Beats")   # Change track
    speaker.change_volume(5)           # Adjust volume
    print(speaker)
