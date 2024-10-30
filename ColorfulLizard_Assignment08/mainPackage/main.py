
 #main.py
from lightPackage import SmartLight
from speakerPackage import SmartSpeaker


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
