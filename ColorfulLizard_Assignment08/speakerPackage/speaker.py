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
