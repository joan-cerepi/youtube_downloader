from pytube import YouTube, Playlist
from pytube.exceptions import *
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
        except VideoUnavailable:
            print('Video is not available.')
            sys.exit(0)
        except RegexMatchError:
            print('The link does not seem to be quite right.')
            print('Correct the link and run the code again.')
            sys.exit(0)
        YouTube(self.url).streams.get_highest_resolution().download(self.path)
        