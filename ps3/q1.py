"""
We have a Media Player application that can play only MP3 files. Now
we want to support MP4 and VLC formats, but their players have
different interfaces.
"""

from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def play(self, file_name):
        pass

class MP3Player(MediaPlayer):
    def play(self, file_name):
        print(f"Playing mp3 file : {file_name}")

class MP4Player(MediaPlayer):
    def play(self, file_name):
        print(f"Playing mp4 file : {file_name}")

class VLCPlayer(MediaPlayer):
    def play(self, file_name):
        print(f"Playing vlc file : {file_name}")

class MediaAdapter:
    def __init__(self, audio_type):
        if audio_type.lower() == "mp4":
            self.player = MP4Player()
        elif audio_type.lower() == "vlc":
            self.player = VLCPlayer()
        elif audio_type.lower() == "mp3":
            self.player = MP3Player()
        else:
            raise ValueError("Unsupported media type")

    def play(self, file_name):
        self.player.play(file_name)
        
        
def main():
    audio_type = input("Enter the audio type (mp3, mp4, vlc): ")
    file_name = input("Enter the file name: ")

    try:
        adapter = MediaAdapter(audio_type)
        adapter.play(file_name)
    except ValueError as e:
        print(e)
        

main()