from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable, RegexMatchError
import sys


class Video:
    '''Create a youtube video class.'''
    def __init__(self, url: str, path: str):
        '''Initialize url and path to the Video class.'''
        self.url = url
        self.path = path
    
    
    def get_url(self):
        '''Access and return your video url.'''
        return self.url
    
    
    def download(self):
        '''Download Video into the given path.'''
        try:
            YouTube(self.url)
        except (VideoUnavailable, RegexMatchError):
            print('Video not found.')
            sys.exit(0)
        YouTube(self.url).streams.get_highest_resolution().download(self.path)
        