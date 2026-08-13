"""
A video streaming platform to play videos with its core content and
allow features like subtitles, different language audio tracks, video
quality options, and audio enhancements etc.

Use decorator pattern to add these features.
"""

from abc import ABC, abstractmethod

class VideoPlayer(ABC):
    @abstractmethod
    def play(self):
        pass
    
    
class BasicVideoPlayer(VideoPlayer):
    def play(self):
        print("Playing video with basic features.")
        
        
class VideoPlayerDecorator(VideoPlayer):
    def __init__(self, video_player):
        self.video_player = video_player

    @abstractmethod
    def play(self):
        pass
    
    
class SubtitlesDecorator(VideoPlayerDecorator):
    def play(self):
        self.video_player.play()
        print("Adding subtitles feature.")
        
        
class AudioTracksDecorator(VideoPlayerDecorator):
    def play(self):
        self.video_player.play()
        print("Adding different language audio tracks feature.")
        
        
class AudioEnhancementsDecorator(VideoPlayerDecorator):
    def play(self):
        self.video_player.play()
        print("Adding audio enhancements feature.")
        

def main():
    basic_player = BasicVideoPlayer()
    print("Basic Video Player:")
    basic_player.play()

    print("\nVideo Player with Subtitles:")
    subtitles_player = SubtitlesDecorator(basic_player)
    subtitles_player.play()

    print("\nVideo Player with Subtitles and Audio Tracks:")
    audio_tracks_player = AudioTracksDecorator(subtitles_player)
    audio_tracks_player.play()

    print("\nVideo Player with Subtitles, Audio Tracks, and Audio Enhancements:")
    audio_enhancements_player = AudioEnhancementsDecorator(audio_tracks_player)
    audio_enhancements_player.play()
    
    
main()