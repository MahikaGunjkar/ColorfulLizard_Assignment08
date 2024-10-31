# Name: Mahika Gunjkar, Nandini Agrawal, Ishani Roy Chowdhury
# email:  gunjkamg@mail.uc.edu, Agarwand@mail.uc.edu, roychoii@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   10/31/2024
# Course #/Section:  4010- 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Team assignment based on real-life example like home techonology. We wrote code to correlate a few home techonologies together

# Brief Description of what this module does. In this speaker.py module, we are describing the different jobs the speaker can perform. We are showing that the volume and track can be changed while also showing stating what the current track or volume are set to.
# Citations:
# Anything else that's relevant:

# speaker.py

class SmartSpeaker:
    def __init__(self, volume=5, track_name="Ambient Sounds"):
        self._volume = volume
        self._track_name = track_name

    def __str__(self):
        return f"SmartSpeaker(volume={self._volume}, track_name='{self._track_name}')"
    
    def __repr__(self):
        return f"SmartSpeaker({self._volume}, '{self._track_name}')"

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        if 0 <= value <= 10:
            self._volume = value
        else:
            print("Volume should be between 0 and 10")

    @property
    def track_name(self):
        return self._track_name
    
    @track_name.setter
    def track_name(self, value):
        self._track_name = value
        
    def play_music(self, track_name):
        self.track_name = track_name
        print(f"Now playing: {self.track_name}")
        
    def change_volume(self, change):
        new_volume = self.volume + change  # Use self.volume to access the property
        if 0 <= new_volume <= 10:
            self.volume = new_volume  # Use the setter
            print(f"Volume set to {self.volume}.")
        else:
            print("Volume change is out of range.")
